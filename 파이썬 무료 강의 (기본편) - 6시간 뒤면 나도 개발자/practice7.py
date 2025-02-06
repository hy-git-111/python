# 함수 가변인자 사용 예제
# 프로필 출력 프로그램

def profile(name, age, *stack):
    print("이름 : {0}\t 나이 : {1}\t".format(name, age), end="")
    for stk in stack:
        print(stk, end="")
    print()

profile("홍길동", 12, "Java")
profile("제니", 23, "Java", "JS", "Kotlin", "Python")
