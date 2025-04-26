# 문장 입력 후 버튼 클릭 시 입력값의 p태그 추가

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
url = "http://localhost:5500/dynamic_element_3.html"
driver.get(url)

submit_el = driver.find_element(By.ID, 'submitBtn')
input_el = driver.find_element(By.ID, 'userInput')

driver.execute_script("""
    arguments[0].addEventListener('click', () => {
        const text = arguments[1].value;
                      
        const elem = document.createElement('p');
        elem.textContent = text;       
        document.body.appendChild(elem);
        return text;
    });
""", submit_el, input_el)
time.sleep(15)