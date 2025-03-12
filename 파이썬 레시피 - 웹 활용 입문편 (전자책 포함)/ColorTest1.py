# 색맹테스트 자동화

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from pprint import pprint
from collections import Counter

url = "https://zzzscore.com/color/"
driver = webdriver.Chrome()
driver.get(url)
driver.implicitly_wait(10)
driver.maximize_window()

# def clikBtn():
n = 1
btns = driver.find_elements(By.XPATH, '//*[@id="grid"]/div')
# print(len(btns))
# print(btns[5].value_of_css_property('background-color'))

def analysis():
    btn_rgba = [ btn.value_of_css_property('background-color') for btn in btns]
    # pprint(btn_rgba)
    result = Counter(btn_rgba)
    # pprint(result)

    for key, value in result.items():
        if value == 1:
            answer = key
            break
        else:
            answer = None
    if answer:  # Python 변수 스코프 규칙 : 반복문 내에서 선언된 변수는 함수 외부에서도 접근할 수 있다.
        index = btn_rgba.index(answer)
        btns[index].click()

start = time.time()
print(start)

while time.time() - start <= 60:
    analysis()

time.sleep(2)
driver.quit()