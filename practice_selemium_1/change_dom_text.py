# DOM의 텍스트 변경하기

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
url = "http://127.0.0.1:5500/change_dom_text.html"
driver.get(url)

driver.execute_script("""
    document.getElementById("greeting").innerText = "안녕하세요!";
""")