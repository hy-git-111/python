from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


url = "https://www.youtube.com/?hl=ko&gl=KR&app=desktop"
driver = webdriver.Chrome()
driver.get(url)
time.sleep(3)

search = driver.find_element(By.XPATH, '//*[@id="center"]/yt-searchbox/div[1]/form/input')
search.send_keys('멍개구름')
time.sleep(1)

search.send_keys(Keys.ENTER)
time.sleep(3)