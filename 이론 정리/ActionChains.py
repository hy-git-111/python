from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

# 액션체인 객체 생성
driver = webdriver.Chrome()
actions = ActionChains(driver)

element = driver.find_element(By.ID, "1")
element_2 = driver.find_element(By.ID, "2")

# 마우스 액션 - 마우스 이동(메서드 체이닝 가능)
actions.move_to_element(element)    # 마우스 오버
actions.move_by_offset(100, 200)    # 현재 마우스 위치에서 x=100, y=200 커서 이동

# 마우스 액션 - 마우스 클릭(메서드 체이닝 가능)
actions.click(element)          # element : 요소 클릭, None : 현재 마우스 위치 클릭
actions.context_click(element)  # element : 요소 마우스 우클릭, None : 현재 마우스 위치에서 우클릭
actions.double_click(element)   # element : 요소 더블클릭, None : 현재 마우스 위치에서 더블클릭

actions.click_and_hold(element=None)    # 마우스 버튼 누른 상태 유지
actions.release(element=None)           # 누르고 있던 마우스 떼기

# 마우스 액션 - 마우스 드래그 앤 드롭(메서드 체이닝 가능)
actions.drag_and_drop(element, element_2)   # source 요소를 target 요소로 드래그 앤 드롭
actions.drag_and_drop_by_offset(element, 100, 200)  # 요소를 x=100, y=200 만큼 드래그

# 액션 종료
actions.perform()   # 액션체인 가장 마지막에 추가할것

# 키보드 액션
from selenium.webdriver.common.keys import Keys

input = driver.find_element(By.ID, "id")
input.send_keys(Keys.ENTER) # 엔터 입력
input.send_keys(Keys.RETURN)# 엔터 입력

input.send_keys(Keys.TAB)   # 탭 입력
input.send_keys(Keys.SPACE) # 스페이스 입력
input.send_keys(Keys.ARROW_UP)  # ARROW_UP : ↑ / ARROW_DOWN : ↓ / ARROW_LEFT : ← / ARROW_RIGHT : →
input.send_keys(Keys.CONTROL, 'c') # ctrl + c
input.send_keys(Keys.F1)    # F1 키 입력

