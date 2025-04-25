# 버튼 클릭하면 문장 요소 동적으로 추가되는 코드

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
url = "http://127.0.0.1:5500/dynamic_element_2.html"
driver.get(url)

btn_elem = driver.find_element(By.ID, 'btn')

driver.execute_script("""
    let count = 0;
                      
    arguments[0].addEventListener('click', () => {
        
        new_elem = document.createElement('p');
        document.body.appendChild(new_elem).textContent = `${count}번째 문장입니다.`;
        return count++;
    });
""", btn_elem)

time.sleep(15)