"""
📌 문제 1: 문자열 뒤집기 (Reverse String)
문제 설명
주어진 문자열 s를 뒤집어 반환하는 함수를 작성하세요.

예제 입력 & 출력

reverse_string("hello")  # 출력: "olleh"
reverse_string("Python")  # 출력: "nohtyP"
reverse_string("a")  # 출력: "a"
reverse_string("")  # 출력: ""

"""

# 방법 1 : for문 사용
def reverse_string(s):
    length = len(s)
    new_s = []

    for i in range(length):
        n = length-i-1
        text = s[n]
        new_s.append(text)
    print(''.join(new_s))

# 방법 2 : reverse() 함수 사용
# def reverse_string(s):
#     list_s = list(s)
#     list_s.reverse()
#     print(list_s)

# 공통 : 함수 실행
reverse_string("hello")  # 출력: "olleh"
# reverse_string("Python")  # 출력: "nohtyP"
# reverse_string("a")  # 출력: "a"
# reverse_string("")  # 출력: ""