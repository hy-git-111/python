# 색맹테스트 자동화

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
# from pprint import pprint
# from collections import Counter

url = "https://zzzscore.com/color/"
driver = webdriver.Chrome()
driver.get(url)
driver.implicitly_wait(10)
driver.maximize_window()

start = time.time()

while time.time() - start <= 60:
    try:
        btn = driver.find_element(By.CLASS_NAME, "main")
        btn.click()
    except:
        pass

time.sleep(3)
driver.quit()
