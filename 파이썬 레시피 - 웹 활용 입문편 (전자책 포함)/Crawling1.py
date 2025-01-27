# 위키독스 도서 페이지의 목차를 크롤링하는 코드

from bs4 import BeautifulSoup as bs # 트리 구조로 데이터 파싱하는데 사용함
from pprint import pprint
import requests

url = 'https://wikidocs.net/35948'
html = requests.get(url)
# pprint(html.text)

soup = bs(html.text,'html.parser')  # 웹 페이지 html 크롤링
# pprint(soup)

data1 = soup.find('div',{'class':'col-sm-3 sidebar'})   # 목차 html 크롤링
# pprint(data1)

data2 = data1.findAll('span',{'style':'padding-left:20px'}) # 목차 html 크롤링
#pprint(data2)

# 목차의 text를 추출하여 리스트에 저장
list = []
for i in data2:
    list.append(i.text.strip())
pprint(list)

html.close()