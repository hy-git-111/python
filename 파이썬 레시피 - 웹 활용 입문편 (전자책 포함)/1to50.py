# 순발력 게임 자동화

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

url = "https://zzzscore.com/1to50/"
driver = webdriver.Chrome()
driver.get(url)
driver.implicitly_wait(10)
driver.maximize_window()

num = 1

def clickBtn():
    global num
    btns = driver.find_elements(By.XPATH, '//*[@id="grid"]/div[*]')

    for btn in btns:
        # print(btn.text)
        if btn.text == str(num):
            btn.click()
            num += 1
            return

while num <= 50:
    clickBtn()

time.sleep(5)
quit()