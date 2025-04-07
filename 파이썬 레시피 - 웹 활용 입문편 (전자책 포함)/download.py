# 이미지 다운로드

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import re
from urllib.request import urlretrieve

options = webdriver.ChromeOptions()
options.add_argument('--headless')


url = "https://www.twitch.tv/god_lita"
driver = webdriver.Chrome(options = options)
driver.implicitly_wait(10)

driver.get(url)

time.sleep(3)

url_element = driver.find_element(By.TAG_NAME, "img")
img_url = url_element.get_attribute("src")
# print(img_url)

title = driver.find_element(By.CSS_SELECTOR, "#live-channel-stream-information > div > div > div.Layout-sc-1xcs6mc-0.kYbRHX > div.Layout-sc-1xcs6mc-0.evfzyg > div.Layout-sc-1xcs6mc-0.denZNh.metadata-layout__support > div.Layout-sc-1xcs6mc-0.jjAyLi > div > a > h1").text
title = re.sub("[^0-9a-zA-Zㄱ-힗]", "", title)
print(title)

urlretrieve(img_url, title+".jpg")
driver.quit()