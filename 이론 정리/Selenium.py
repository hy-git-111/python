# 브라우저 실행
from selenium import webdriver

driver = webdriver.Chrome()
url = "https://www.google.com"
driver.get(url)

# 브라우저 옵션 설정
from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument("--headless")

driver = webdriver.Chrome(options=options)
"""
셀레니움 옵션
--headless      : GUI 없이 브라우저 실행, 리소스 절약 가능, 병렬실행이나 젠킨스 사용 시 사용
--start-maximized : 브라우저 최대화
--disable-popup-blocking : 팝업 차단 비활성화, 페이지 로딩 속도 감소
--disable-notifications : 브라우저 알림 비활성화
"""

# 정적 요소 찾기(동적 요소는 js를 사용하여 Interactable 후 찾기)
from selenium.webdriver.common.by import By

element = driver.find_element(By.CSS_SELECTOR, "css_selector")  # str로 반환
element = driver.find_elements(By.CSS_SELECTOR, "css_selector") # 리스트로 반환

# XPATH로 텍스트 기준 정적 요소 찾기
# // : 상대 경로, / : 절대 경로, @ : 속성
from selenium.webdriver.common.by import By

element = driver.find_element(By.XPATH, '//div[@id="ID"]')  # id가 'ID'인 div 태그를 찾아 반환
element = driver.find_element(By.XPATH, '//div[text()="찾을 텍스트"]')  # '찾을 텍스트'가 있는 div 태그를 찾고, 직접 포함된 텍스트만 반환
element = driver.find_element(By.XPATH, '//div[contains(@class, "찾을 텍스트")]')   # class(속성)에 '찾을 텍스트'가 포함된 div 태그 찾기, 자식태그가 있는 경우, 안정적인 탐색을 위해 요소 내부의 모든 텍스트를 하나의 문자열로 변환하여 '찾을 텍스트' 탐색
element = driver.find_element(By.XPATH, '//div[(text()="찾을 텍스트") and contains(@class, "찾을 텍스트")]')    # 텍스트가 '찾을 텍스트'이고 클래스 속성에 '찾을 텍스트'가 표함된 div 태그 찾기

element = driver.find_element(By.XPATH, '//span[normalize-space()="찾을 텍스트"]')  # 앞/뒤/중간 공백 정규화 후 텍스트가 "텍스트"인 span 태그 반환(^^새^^소^식^^바로가기^^^ > 새소식 바로가기)
element = driver.find_element(By.XPATH, '//span[contains(normalize-space(), "찾을 텍스트")]')   # '찾을 텍스트'가 포함된 div 태그를 찾고, 문자열의 앞뒤 공백을 제거한 후 연속된 공백을 하나의 공백으로 변환하여 반환(^^안^^^녕^^^!^^ > 안^녕^!)

element = driver.find_element(By.XPATH, '//*[@data-testid="login-button"]') # data- 속성을 활용하면 고유속성처럼 사용할 수 있음(유지보수 용이)
element = driver.find_element(By.XPATH, '//div[starts-with(@id, "user")')   # id가 "user"로 시작하는 input 반환

element = driver.find_elements(By.XPATH, '(//li)[last()]')   # <li> 목록 중 마지막 요소 반환
element = driver.find_elements(By.XPATH, '(//table/tbody/tr)[position()=3]')    # 테이블의 세 번째 행 요소 반환

# XPATH로 조상 요소 찾기, ancestor:: 명시 필요
from selenium.webdriver.common.by import By

element = driver.find_element(By.ID, 'element') # 기준 요소
ancestor = element.find_elements(By.XPATH, 'ancestor::div[@class="rct-collapse-btn"]')

# XPATH로 부모 요소 찾기, parent:: 명시 필요
from selenium.webdriver.common.by import By

element = driver.find_element(By.XPATH, '//button[contains(@class, "rct-collapse-btn") and parent::div]')   # 기본 정석
child = driver.find_element(By.XPATH, '//button[contains(@class, "rct-collapse-btn")]') # 버전 2
parent = child.find_element(By.XPATH, '..') # .. = parent::node()

# XPATH로 형제 요소 찾기, sibling:: 명시
from selenium.webdriver.common.by import By

sibling = driver.find_element(By.XPATH, '//div[@class="class-name1" and text()="텍스트"]')
next_sibling = sibling.find_element(By.XPATH, './/following-sibling::div[@class="class-name2"]')    # 현재 노드 뒤에 있는 형제 요소
before_sibling = sibling.find_element(By.XPATH, './/preceding-sibling::span[@class="rct-checkbox"]')    # 현재 노드 앞에있는 형제 요소

# XPATH로 자식 요소 찾기
from selenium.webdriver.common.by import By

parent = driver.find_element(By.ID, 'parent')
child = parent.find_element(By.XPATH, './/child::button[contains(@class, "rct-collapse-btn")]') # 기본 정석
child = parent.find_element(By.XPATH, './/button[contains(@class, "rct-collapse-btn")]')    # 생략 버전

# XPATH로 자손 요소 찾기
from selenium.webdriver.common.by import By

parent = driver.find_element(By.ID, 'parent')
descendant = parent.find_elements(By.XPATH, './/descendant::span[@class="rct-checkbox"]')   # 기본 정석
descendant = parent.find_element(By.XPATH, './/span[@class="rct-checkbox"]')   # 생략 버전

# XPATH로 모든 앞/뒤 요소 찾기
from selenium.webdriver.common.by import By

current_element = driver.find_element(By.ID, '//td[text()="1"]')
following = current_element.find_element(By.XPATH, 'following::td[1]')
preceding = current_element.find_element(By.XPATH, 'preceding::td[1]')

# CSS SELECTOR로 요소 찾기 - 속성 선택자 방식(태그[속성="속성값"])
from selenium.webdriver.common.by import By

element = driver.find_elements(By.CSS_SELECTOR, 'button[class]') # class값과 상관없이 class 속성을 가진 모든 button 요소 탐색
element = driver.find_elements(By.CSS_SELECTOR, 'button[class="class_1"][id="ID"]')    # class 속성과 id 속성을 가진 모든 button 요소 탐색

element = driver.find_element(By.CSS_SELECTOR, 'button[class^="class"]')    # class 속성값이 "class"로 시작하는 요소
element = driver.find_element(By.CSS_SELECTOR, 'button[class$="1"]')    # class 속성값이 "1"로 끝나는 요소

element = driver.find_element(By.CSS_SELECTOR, 'button[class~="class_name_1"]')   # class 속성값이 "class_name_1"이거나 다중 속성값 중 "class_name_1"이 포함되는 요소
element = driver.find_element(By.CSS_SELECTOR, 'button[class*="class"]')    # class 속성값의 일부에 "class"가 포함되는 요소

element = driver.find_elements(By.CSS_SELECTOR, 'div p') # 자손 선택자, <div> 태그 하위에 있는 모든 <p> 태그 요소 탐색
element = driver.find_element(By.CSS_SELECTOR, 'div+p') # 인접 형제 선택자, <div> 태그와 바로 이웃하는 형제요소 중 <p> 태그인 형제 요소 탐색
element = driver.find_elements(By.CSS_SELECTOR, 'div~p') # 일반 형제 선택자, <div> 태그의 형제요소 중 <p> 태그인 형제 요소 모두 탐색

# CSS SELECTOR로 요소 찾기 - 클래스 체인 방식
from selenium.webdriver.common.by import By

element = driver.find_element(By.CSS_SELECTOR, 'button.class')    # class 속성값이 "class"로 시작하는 요소

# CSS SELECTOR로 요소 찾기 - 가상 클래스
from selenium.webdriver.common.by import By

element = driver.find_elements(By.CSS_SELECTOR, 'li:first-child')    # <li> 목록 중, 첫 번째 <li> 요소 탐색(li목록이 여러개일경우 여러개의 요소 반환됨)
element = driver.find_elements(By.CSS_SELECTOR, 'button:last-child')    # <button> 목록 중, 마지막 <button> 요소 탐색
element = driver.find_elements(By.CSS_SELECTOR, 'div:nth-child(1)')    # <div> 목록 중, 첫 번째 <div> 요소 탐색
element = driver.find_elements(By.CSS_SELECTOR, 'tr:nth-child(odd)')    # <tr> 목록 중, 홀수 번째 <tr> 요소 탐색(odd number : 홀수)
element = driver.find_elements(By.CSS_SELECTOR, 'tr:nth-child(2n)')    # <tr> 목록 중, 짝수 번째 <tr> 요소 탐색(even number : 짝수)
element = driver.find_elements(By.CSS_SELECTOR, 'input:enabled')    # 활성화된 <input> 요소
element = driver.find_elements(By.CSS_SELECTOR, 'input:disabled')    # 비활성화된 <input> 요소
element = driver.find_elements(By.CSS_SELECTOR, 'input:checked')    # 체크된 <input> 요소
element = driver.find_elements(By.CSS_SELECTOR, 'input:not([checked])')    # 체크되지 않은 모든 <input> 요소

# 동적 요소 찾기
from selenium.webdriver.common.by import By
import datetime

today = datetime.date.today().strftime("%Y-%m-%d")
element = driver.find_element(By.XPATH, f"//div[text()='{today}']")

# 대기
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver.implicitly_wait(10)  # Implicit Wait, 암시적 대기, 요소 탐색 시 최대 대기 시간 지정

wait = WebDriverWait(driver, timeout=10, poll_frequency=0.5, ignored_exceptions=None)   # Explicit Wait, 명시적 대기, 특정 조건 충족 시까지 대기(driver, 대기시간, 재확인 주기, 무시할 예외 지정)

wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "css_selector"))) # 눈에 보일때까지 대기
wait.until(EC.invisibility_of_element_located((By.CSS_SELECTOR, "css_selector")))   # 눈에 안보일때까지 대기
wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "css_selector")))   # 요소 위치가 나타날때까지 대기(표시 여부와 무관하게 html에 요소가 추가된경우)

wait.until(EC.text_to_be_present_in_element((By.ID, "id"), "text"))    # 요소의 text 속성에 "text"가 포함될때까지 대기
wait.until(EC.text_to_be_present_in_element_value((By.ID, "id"), "text"))   # 요소의 valu 속성에 "text"가 포함될때까지 대기

wait.until(EC.element_to_be_clickable((By.ID, "id")))   # 버튼/input 요소가 클릭 가능할 때까지 대기
wait.until(EC.element_to_be_selected(element))  # 체크박스/라디오버튼 요소가 선택 가능할 때까지 대기

wait.until(EC.number_of_windows_to_be(2))   # 브라우저 수가 2개가 될때까지 대기(새 창으로 열기/닫기 시 사용)
wait.until(EC.staleness_of(element))    # 요소의 상태가 변경될때까지 대기
wait.until(EC.element_to_be_clickable)

# 새로고침
driver.refresh()    # 페이지 새로고침을 하면 브라우저가 새로운 HTML을 로드한다.

# 새로고침 전 : 특정 요소에 메모리 주소(참조)를 저장
# 새로고침 후 : 기존 페이지의 DOM이 완전히 다시 로드됨 → 기존 요소는 삭제됨.
# 하지만 selenium은 삭제된 요소의 참조를 유지하고 있음 → 더 이상 존재하지 않는 요소를 가리킴.
# 따라서 StaleElementReferenceException 오류 발생

# 이를 해결하기 위해 새로고침 후 요소를 다시 불러와야 함

# 스크린샷 저장
from selenium.webdriver.common.by import By

element = driver.find_element(By.TAG_NAME, "body")
element.save_screenshto()("/screenshot.png")    # <body> 태그를 스크린샷하면 스크롤바가 찍힘

driver.save_screenshot("/screenshot.png")    # 스크롤바가 스크린샷에 찍히지 않음

# 텍스트 추출
from selenium.webdriver.common.by import By

element = driver.find_element(By.CLASS_NAME, "className")
normal_text = element.text  # .text : 정적 텍스트 추출
hidden_text = element.get_attribute("textContent")  # .get_attribute() : 태그의 속성을 추출 > 숨겨진 텍스트 추출 가능, get_attribute("textContent") : 동적 텍스트 추출

# 드롭다운 선택
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By

dropdown = Select(driver.find_element(By.ID, "id"))
dropdown.select_by_visible_text("option")
dropdown.select_by_value("option")
dropdown.select_by_index("1")

# HTML 폼 요소 자동화 - 파일 업로드
from selenium.webdriver.common.by import By

input = driver.find_element(By.ID, "id")
input.send_keys("D:\Hyeyoung\Web")

# 얼럿창 처리
alert = driver.switch_to.alert  # 현재 뜬 alert로 전환
alert_text = alert.text # alert 텍스트 확인

alert.accept()  # alert / confirm 확인 선택
alert.dismiss() # confirm 취소 선택
alert.send_keys("inputValue")   # 프롬프트 입력

# iframe 처리 (<iframe> : HTML 내부에 다른 HTML 페이지 삽입)
# 모든 창 핸들 가져오기 > for 새 창 in 모든 창 > 새 창으로 전환 > 작업 후 원래 창 또는 최상위 프레임으로 전환
driver.window_handles               # 모든 창 핸들 가져오기
driver.switch_to.window(new_window_handle)  # 새 핸들(새 창)로 포커스 전환(WebElement 객체 / id / name 속성 / 인덱스 전달 가능)
driver.switch_to.parent_frame()     # 상위 프레임으로 전환
driver.switch_to.default_content()  # 최상위 프레임으로 전환



# UI 변경 확인 : is_displayed()
from selenium.webdriver.common.by import By

message = driver.find_element(By.ID, "message")
if message.is_displayed():
    print("메시지가 정상적으로 표시되었습니다.")

# 체크박스 선택 확인 : is_selected()
checkbox = True
if not checkbox.is_selected():
    checkbox.click()

# 버튼 활성화 확인 : is_enabled()
from selenium.webdriver.common.by import By

button = driver.find_element(By.ID, "submit_btn")
if button.is_enabled():
    button.click()



# 쿠키 처리
from selenium import webdriver

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

# 현재 페이지의 html 가져오기
html = driver.page_source

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
from selenium import webdriver

driver = webdriver.Chrome()
driver.execute_script("JavaScript")

# 페이지 스크롤(상대좌표)
driver.execute_script("window.scrollBy(x, y);") # 현재 스크롤 위치에서 x, y축으로 이동(단위 : 픽셀)

# 페이지 스크롤(절대좌표)
driver.execute_script("window.scrollTo(x, y);") # 좌표(0, 0)에서 x, y축으로 이동(단위 : 픽셀)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")  # 스크롤 길이만큼 스크롤(= 화면을 맨 아래까지 스크롤)

# 특정 요소까지 스크롤 이동
from selenium.webdriver.common.by import By

element = driver.find_element(By.XPATH, "targetElement")
driver.execute_script("arguments[0].scrollIntoView(true);", element)    # 요소가 뷰포트에 보일때까지 스크롤(true : 최상단 / false : 최하단)
driver.execute_script("arguments[0].scrollIntoView({ behavior: 'smooth', block: 'start' });", element)  # 요소가 뷰포트에 보일때까지 부드럽게 스크롤(start : 최상단 / center : 화면 중앙 / end : 최하단)


# 숨겨진 요소 찾기
driver.execute_script("arguemnts[0].style.display = 'black';", hidden_input)    # 'display:none' 상태의 요소에는 적용 불가 

# 요소 표시 상태 확인
status = driver.execute_script("return document.getElementById('comfirmation_message').style.display;")

# 요소 속성값 가져오기
driver.execute_script("return arguments[0].value;", element)

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



