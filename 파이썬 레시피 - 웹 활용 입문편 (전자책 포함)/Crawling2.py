# 유튜브 > 인기 급상승 > 인기 급상승 TOP 5 채널명 크롤링

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from bs4 import BeautifulSoup as bs
import datetime

driver = webdriver.Chrome()
url = 'https://www.youtube.com/'
driver.get(url)
driver.maximize_window()

WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "#endpoint > tp-yt-paper-item"))
)

# 인기 급상승 페이지 진입
element = driver.find_element(By.LINK_TEXT, "인기 급상승").click()
# time.sleep(5)

WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "#text > a"))
)

# 웹페이지 채널명 크롤링
html = driver.page_source
soup = bs(html, 'html.parser')

channels = soup.select("a.yt-simple-endpoint.style-scope.yt-formatted-string")[:10] # HTML 요소(태그) 리스트 반환

# 순서 유지하여 중복 제거
channels_top5 = []
for i in channels:
    text = i.text.strip()
    if text and text not in channels_top5:
        channels_top5.append(text)
# print(channels_top5)

time.sleep(2)
driver.quit()
# channels_top5 = ['NFL', 'VIVINOS', '스브스 예능맛집', '김숙티비kimsookTV', 'MrBeast']

# 순위출력
now = datetime.datetime.now()
print("인기 급상승 콘텐츠 채널 목록\n확인일 : {0}\n".format(now.strftime("%Y-%m-%d")))

n = 1
for i in channels_top5:
    print("{0}위 : {1}".format(n, channels_top5[n-1]))
    n += 1