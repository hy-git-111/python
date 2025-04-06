# 버튼을 클릭할때마다 요소 추가하기

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
url = "http://127.0.0.1:5500/dynamic_element_1.html"
driver.get(url)

btn_elem = driver.find_element(By.ID, 'btn')

driver.execute_script("""
    arguments[0].addEventListener('click', () => {
        elem = document.createElement('p');
        document.body.appendChild(elem).innerText = "이벤트로 추가된 문장입니다";
    });
""", btn_elem)

time.sleep(10)