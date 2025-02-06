# 함수 기본값, 키워드값 예제
# 프로필 출력 프로그램

def profile(name, age=15, stack="파이썬"):  # 기본값 지정
    print("이름 : {0}\t 나이 : {1}\t 주 사용 언어 : {2}".format(name, age, stack), end="")

profile("홍길동", 12, "Java")
profile("제니") # 기본값 출력
profile(age = 50, name = "김남길") # 키워드값으로 함수 호출
