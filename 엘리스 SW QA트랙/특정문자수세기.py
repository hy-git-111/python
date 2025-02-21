"""
📌 문제 2: 특정 문자 개수 세기 (Count Character)
문자열 s와 특정 문자 char가 주어질 때, 해당 문자가 문자열에 몇 번 등장하는지 반환하는 함수를 작성하세요.

예제 입력 & 출력
count_character("banana", "a")  # 출력: 3
count_character("hello world", "l")  # 출력: 3
count_character("Python", "y")  # 출력: 1
count_character("abc", "z")  # 출력: 0

"""

def count_character(s, char):
    cnt = 0
    for text in s:
        if text == char:
            cnt += 1
    print(cnt)

count_character("banana", "a")  # 출력: 3
count_character("hello world", "l")  # 출력: 3
count_character("Python", "y")  # 출력: 1
count_character("abc", "z")  # 출력: 0
