# 브라우저 실행
from Selenium import webdriver

driver = webdriver.Chrome()
url = "https://www.google.com"
driver.get(url)

# 정적 요소 찾기(동적 요소는 js를 사용하여 Interactable 후 찾기)
from Selenium.webdriver.common.by import By

element = driver.find_element(By.CSS_SELECTOR, "css_selector")  # str로 반환
element = driver.find_elements(By.CSS_SELECTOR, "css_selector") # 리스트로 반환

# XPATH로 텍스트 기준 정적 요소 찾기
from Selenium.webdriver.common.by import By

element = driver.find_element(By.XPATH, '//div[text()="찾을 텍스트"]')  # '찾을 텍스트'가 있는 div 태그를 찾고, 직접 포함된 텍스트만 반환
element = driver.find_element(By.XPATH, '//div[contains(@class, "찾을 텍스트")]')  # class(속성)에 '찾을 텍스트'가 포함된 div 태그 찾기, 자식태그가 있는 경우, 안정적인 탐색을 위해 요소 내부의 모든 텍스트를 하나의 문자열로 변환하여 '찾을 텍스트' 탐색
element = driver.find_element(By.XPATH, '//div[contains(normalize-space(), "찾을 텍스트")]')  # '찾을 텍스트'가 포함된 div 태그를 찾고, 문자열의 앞뒤 공백을 제거한 후 연속된 공백을 하나의 공백으로 변환하여 반환(^^안^^^녕^^^!^^ > 안^녕^!)

# XPATH로 형제 요소 찾기
from Selenium.webdriver.common.by import By

one_sibling = driver.find_element(By.XPATH, '//div[@class="class-name1" and text()="텍스트"]')
the_other_sibling = one_sibling.find_element(By.XPATH, 'following-sibling::div[@class="class-name2"]')

# 동적 요소 찾기
from Selenium.webdriver.common.by import By
import datetime

today = datetime.date.today().strftime("%Y-%m-%d")
element = driver.find_element(By.XPATH, f"//div[text()='{today}']")

# 대기
from Selenium.webdriver.common.by import By
from Selenium.webdriver.support.ui import WebDriverWait
from Selenium.webdriver.support import expected_conditions as EC

wait = WebDriverWait(driver, 10)
element = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "css_selector"))) # 요소가 클릭 가능할 때까지 대기
element = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "css_selector")))   # 눈에 보일때까지 대기
element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "css_selector"))) # 요소 위치가 나타날때까지 대기(표시 여부와 무관하게 html에 요소가 추가된경우)

# 새로고침
driver.refresh()    # 페이지 새로고침을 하면 브라우저가 새로운 HTML을 로드한다.

# 새로고침 전 : 특정 요소에 메모리 주소(참조)를 저장
# 새로고침 후 : 기존 페이지의 DOM이 완전히 다시 로드됨 → 기존 요소는 삭제됨.
# 하지만 Selenium은 삭제된 요소의 참조를 유지하고 있음 → 더 이상 존재하지 않는 요소를 가리킴.
# 따라서 StaleElementReferenceException 오류 발생

# 이를 해결하기 위해 새로고침 후 요소를 다시 불러와야 함

# 스크린샷 저장
from Selenium.webdriver.common.by import By

element = driver.find_element(By.TAG_NAME, "body")
element.save_screenshto()("/screenshot.png")    # <body> 태그를 스크린샷하면 스크롤바가 찍힘

driver.save_screenshot("/screenshot.png")    # 스크롤바가 스크린샷에 찍히지 않음

# 텍스트 추출
from Selenium.webdriver.common.by import By

element = driver.find_element(By.CLASS_NAME, "className")
normal_text = element.text  # .text : 정적 텍스트 추출
hidden_text = element.get_attribute("textContent")  # .get_attribute() : 태그의 속성을 추출 > 숨겨진 텍스트 추출 가능, get_attribute("textContent") : 동적 텍스트 추출

# 드롭다운 선택
from Selenium.webdriver.support.ui import Select
from Selenium.webdriver.common.by import By

dropdown = Select(driver.find_element(By.ID, "id"))
dropdown.select_by_visible_text("option")

# HTML 폼 요소 자동화 - 파일 업로드
from Selenium.webdriver.common.by import By

input = driver.find_element(By.ID, "id")
input.send_keys("D:\Hyeyoung\Web")

# 얼럿창 처리
from Selenium.webdriver.common.alert import Alert

Alert.accept()

# 확인창 처리
from Selenium.webdriver.common.alert import Alert

Alert.accept()  # 확인 선택
Alert.dismiss() # 취소 선택

# 프롬프트
from Selenium.webdriver.common.alert import Alert

Alert.send_keys("inputValue")


# UI 변경 확인 : is_displayed()
from Selenium.webdriver.common.by import By

message = driver.find_element(By.ID, "message")
if message.is_displayed():
    print("메시지가 정상적으로 표시되었습니다.")

# 체크박스 선택 확인 : is_selected()
checkbox = True
if not checkbox.is_selected():
    checkbox.click()

# 버튼 활성화 확인 : is_enabled()
from Selenium.webdriver.common.by import By

button = driver.find_element(By.ID, "submit_btn")
if button.is_enabled():
    button.click()

# 쿠키 처리
from Selenium import webdriver

driver = webdriver.Chrome()
url = "www.naver.com"
driver.get(url)

cookie = driver.get_cookie(name)    # 특정 이름의 쿠키 가져오기 
cookies = driver.get_cookies()  # 모든 쿠키 가져오기

driver.add_cookie(  # 쿠키 추가하기
    {
        "name": "user1", 
        "value": "abc123", 
        "domain": "naver.com"
    }
    )

driver.delete_cookie("user1")   # "user1" 쿠키 삭제
driver.delete_all_cookies() # 모든 쿠키 삭제

# 로그 설정
import logging
logging.basicConfig(
    filename="test_result.log",  # 로그 파일 경로
    level=logging.INFO,  # 로그 레벨 설정
    format="%(asctime)s - %(message)s",  # 로그 포맷 지정
    encoding="utf-8"  # ✅ UTF-8 인코딩 적용
)

logging.info("테스트 시작")
logging.warning("UI 요소 변경됨")
logging.error("오류 발생")
logging.exception("예외상황 발생")
logging.info("테스트 종료")

# 자동 검증(assert 조건, 참일떄)
actual_text = "text1"
expected_text = "text100000"
assert actual_text == expected_text, "실제 텍스트와 예상 텍스트가 일치하지 않습니다."
print("UI 변경이 감지되지 않았습니다.")

# 파일 처리
import json

data = {}
with open("data.json", "w", encoding="utf-8") as f:    # w : 쓰기(저장)
    json.dump(data, f, ensure_ascii=False, indent=4)    # 데이터 저장 시, 반복문으로 데이터 누락/중복/비정상 데이터 검사 후 저장하도록 한다.

with open("data.json", "r") as f:   # r : 읽기(불러오기)
    data = json.load(f)

json_string = '''{}'''
python_object = json.loads(json_string)   # JSON 문자열을 파이썬 객체로 불러오기(변환)

python_dict = {}
json_string = json.dumps(python_dict)   # 파이썬 딕셔너리를 JSON 문자열로 처리(변환)

# csv 파일 처리
import csv

csv_data = []
with open("data.csv", "w", encoding="utf-8") as f:  # data.csv를 w모드로 열기(내용 없음)
    writer = csv.writer(f)  # csv 파일을 작성하는 writer 객체 생성 
    writer.writerows(csv_data)  # 리스트의 리스트를 한번에 기록(저장)

with open("data.csv", "r", encoding="utf-8") as f:  # data.csv를 r모드로 열기
    reader = csv.reader(f)  # csv 파일을 작성하는 reader 객체 생성 
    for row in reader:  # 데이터를 한 행씩 처리
        print(row)












# JS를 사용한 동적 페이지 제어
from Selenium import webdriver

driver = webdriver.Chrome()
driver.execute_script("JavaScript")

# 페이지 스크롤(상대좌표)
driver.execute_script("window.scrollBy(x, y);") # 현재 스크롤 위치에서 x, y축으로 이동(단위 : 픽셀)

# 페이지 스크롤(절대좌표)
driver.execute_script("window.scrollTo(x, y);") # 좌표(0, 0)에서 x, y축으로 이동(단위 : 픽셀)

# 특정 요소까지 스크롤 이동
from Selenium.webdriver.common.by import By
element = driver.find_element(By.XPATH, "targetElement")
driver.execute_script("arguments[0].scrollIntoView();", element)

# 숨겨진 요소 찾기
driver.execute_script("arguemnts[0].style.display = 'black';", hidden_input)    # 'display:none' 상태의 요소에는 적용 불가 

# 요소 표시 상태 확인
status = driver.execute_script("return document.getElementById('comfirmation_message').style.display;")

# 날짜/시간 선택 필드 value 직접 주입
date_input = []
driver.execute_script("""
    const input = arguments[0];  
    input.setAttribute('value', arguments[1])
    input.dispatchEvent(new Event('input', { bubbles: true}));
    input.dispatchEvent(new Event('change', { bubbles: true }));
""", date_input, "2025-03-01")  

# 1. date_input, "2025-03-01"   : html <input> 요소인 date_input을 argument[0]에 전달, 날짜를 argument[1]에 전달함
# 2. const input = argument[0];     : input 변수에 date_input 저장
# 3. input.setAttribute('value', arguments[1])  : input 태그의 속성 설정, value를 arguments[1](날짜)로. 브라우저 이벤트 시스템이 감지하지 못해 사람이 한것처럼 이벤트를 발생시켜야함.
# 4. input.dispatchEvent(new Event('input', { bubbles: true}));     : input 이벤트를 dispatch(발생시키기), 새 이벤트는 'input'(입력하기), 옵션은 {bubbles: true}(이벤트가 상위 요소로 전파되도록 설정)
# 5. input.dispatchEvent(new Event('change', { bubbles: true }));   : input 이벤트를 dispatch(발생시키기), 새 이벤트는 'change'(변경하기), 옵션은 {bubbles: true}(이벤트가 상위 요소로 전파되도록 설정)

# input 이벤트 : 사용자가 한 글자라도 입력하거나 삭제하면 발생하는 이벤트, dispatchEvent()로 발생시킬 수 있다.
# change 이벤트 : 사용자가 입력 완료 후 다른 요소를 클릭하거나 Enter를 눌러 포커스를 잃을 때 발생하는 이벤트, dispatchEvent()로 발생시킬 수 있다.

# argument : 인수, 함수를 동작하기 위한 숫자
# parameter : 매개변수, 함수를 동작하기 위한 문자



