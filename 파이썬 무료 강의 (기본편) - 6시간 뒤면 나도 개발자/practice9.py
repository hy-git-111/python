# 주 1회 보고서를 작성해야 한다.
# 1주차부터 50주차까지 보고서 파일을 만드는 프로그램을 작성하시오.

# 파일명 : 1주차.txt

# 양식
# - 1 주차 주간보고 -
# 부서 : 
# 이름 : 
# 업무요약 :

# 변수 선언하여 파일 생성
week1 = list(range(1,51))

for i in week1:
    # 파일 객체를 변서 file에 직접 할당
    file = open(f"{i}주차.txt", "w", encoding="utf-8")  
    file.write("- {i} 주차 주간보고 - \n")
    file.write("부서 : \n")
    file.write("이름 : \n")
    file.write("업무요약 : \n")
    file.close()

# with을 사용하여 파일 생성
week2 = list(range(1,51))

for i in week2:
    # with에서는 file 변수를 선언하지 않음. 
    # 따라서 with에서는 file은 객체를 참조하는 변수이므로 as file: 입력이 필수
    with open(f"{i}주차.txt", "w", encoding="utf-8") as file:    
        file.write("- {i} 주차 주간보고 - \n")
    file.write("부서 : \n")
    file.write("이름 : \n")
    file.write("업무요약 : \n")