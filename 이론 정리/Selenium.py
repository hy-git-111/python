# 브라우저 실행
from selenium import webdriver

driver = webdriver.Chrome()
url = "https://www.google.com"
driver.get(url)

# 정적 요소 찾기(동적 요소는 js를 사용하여 Interactable 후 찾기)
from selenium.webdriver.common.by import By

element = driver.find_element(By.CSS_Selector, "css_selector")  # str로 반환
element = driver.find_elements(By.CSS_Selector, "css_selector") # 리스트로 반환

# 대기
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

WebDriverWait(driver, 10)
element = wait.until(EC.element_to_be_clickable((By.CSS_Selector, "css_selector"))) # 요소가 클릭 가능할 때까지 대기


# confirmation_message = (By.ID, "confirmation_message")
        # 단, expected_conditions은 element가 보일때까지
        # WebDriver가 Wait해준다. 5초만
element = wait.until(EC.visibility_of_element_located((By.CSS_Selector, "css_selector")))   # 눈에 보일때까지 대기
element = wait.until(EC.presence_of_element_located((By.CSS_Selector, "css_selector"))) # 요소 위치가 나타날때까지 대기(표시 여부와 무관하게 html에 요소가 추가된경우)

# 새로고침
driver.refresh()    # 페이지 새로고침을 하면 브라우저가 새로운 HTML을 로드한다.

# 새로고침 전 : 특정 요소에 메모리 주소(참조)를 저장
# 새로고침 후 : 기존 페이지의 DOM이 완전히 다시 로드됨 → 기존 요소는 삭제됨.
# 하지만 Selenium은 삭제된 요소의 참조를 유지하고 있음 → 더 이상 존재하지 않는 요소를 가리킴.
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
normal_text = element.text
hidden_text = element.get_attribute("textContent")  # .get_attribute() : 태그의 속성을 추출 > 숨겨진 텍스트 추출 가능

# 드롭다운 선택
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By

dropdown = Select(driver.find_element(By.ID, "id"))
dropdown.select_by_visible_text("option")

# HTML 폼 요소 자동화 - 파일 업로드
from selenium.webdriver.common.by import By

input = driver.find_element(By.ID, "id")
input.send_keys("D:\Hyeyoung\Web")

# 얼럿창 처리
from selenium.webdriver.common.alert import Alert

Alert.accept()

# 확인창 처리
from selenium.webdriver.common.alert import Alert

Alert.accept()  # 확인 선택
Alert.dismiss() # 취소 선택

# 프롬프트
from selenium.webdriver.common.alert import Alert

Alert.send_keys("inputValue")


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





# JS를 사용한 동적 페이지 제어
from selenium import webdriver

driver = webdriver.Chrome()
driver.execute_script("JavaScript")

# 페이지 스크롤(상대좌표)
driver.execute_script("window.scrollBy(x, y);") # 현재 스크롤 위치에서 x, y축으로 이동(단위 : 픽셀)

# 페이지 스크롤(절대좌표)
driver.execute_script("window.scrollTo(x, y);") # 좌표(0, 0)에서 x, y축으로 이동(단위 : 픽셀)

# 특정 요소까지 스크롤 이동
from selenium.webdriver.common.by import By
element = driver.find_element(By.XPATH, "targetElement")
driver.execute_script("arguments[0].scrollIntoView();", element)

# 숨겨진 요소 찾기
driver.execute_script("arguemnts[0].style.display = 'black';", hidden_input)    # 'display:none' 상태의 요소에는 적용 불가 

# 요소 표시 상태 확인
status = driver.execute_script("return document.getElementById('comfirmation_message').style.display;")