from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import logininfo
import csv
from selenium.webdriver.common.keys import Keys

browser=webdriver.Chrome()
screen_width = browser.execute_script("return window.screen.width;")
screen_height = browser.execute_script("return window.screen.height;")
browser.set_window_size(screen_width, screen_height)
browser.get("https://twitter.com/")
time.sleep(3)

browser.find_element(By.XPATH,"/html/body/div[1]/div/div/div[1]/div/div[1]/div/div/div/div/div[2]/div/div/div[1]/a" ).click()
time.sleep(3)

username=browser.find_element(By.XPATH,"/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input" )
username.send_keys(logininfo.username)
time.sleep(3)

browser.find_element(By.XPATH,"/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]/div" ).click()
time.sleep(2)

pasword=browser.find_element(By.XPATH,"/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input" )
pasword.send_keys(logininfo.password)
time.sleep(3)

# clicks the login button
browser.find_element(By.XPATH,"/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div/div" ).click()
time.sleep(3)

# performs the search
search=browser.find_element(By.XPATH,"/html/body/div[1]/div/div/div[2]/main/div/div/div/div[2]/div/div[2]/div/div/div/div[1]/div/div/div/form/div[1]/div/div/div/label/div[2]/div/input" )
search.send_keys(logininfo.keyword, logininfo.advanced_search)
time.sleep(3)

browser.find_element(By.XPATH,"/html/body/div[1]/div/div/div[2]/main/div/div/div/div[2]/div/div[2]/div/div/div/div[1]/div/div/div/form/div[1]/div/div/div/label/div[2]/div/input").send_keys(Keys.ENTER)

# Latest tweets click
browser.find_element(By.XPATH,"/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[1]/div[1]/div[2]/nav/div/div[2]/div/div[2]/a/div/div/span" ).click()
time.sleep(1)


MAX_TWEETS = 40  # maximum number of tweets
sonuc = []
twit = browser.find_elements(By.XPATH, "//div[@data-testid='tweetText']")
time.sleep(2)
print(str(len(twit)) + "tweet was successfully pulled")
for i in twit:
    sonuc.append(i.text)

tweet_sayac = len(sonuc)
sayac = 0
son = browser.execute_script("return document.documentElement.scrollHeight")
while tweet_sayac < MAX_TWEETS:
    browser.execute_script("window.scrollTo(0,document.documentElement.scrollHeight)")
    time.sleep(5)
    yeni = browser.execute_script("return document.documentElement.scrollHeight")
    if son == yeni :
        break
    son = yeni
    sayac += 1
    twit = browser.find_elements(By.XPATH,"//div[@data-testid='tweetText']")
    time.sleep(15)
    print(str(len(twit)) + "1 tweet was successfully pulled")
    for i in twit:
        sonuc.append(i.text)
        tweet_sayac += 1
        if tweet_sayac >= MAX_TWEETS:
            break

# CSV dosyası oluşturma
with open('Erdoğan.csv', mode='w', encoding='UTF-8', newline='') as file:
    writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    writer.writerow(['Sıra No', 'Tweet Metni'])
    for index, tweet in enumerate(sonuc, start=1):
        writer.writerow([index, tweet])

print(f"{tweet_sayac} tweet was successfully captured and saved")


browser.close()