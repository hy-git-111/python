"""
📌 문제 3: 리스트의 최댓값 찾기 (Find Maximum in List)
문제 설명
주어진 리스트에서 가장 큰 값을 반환하는 함수를 작성하세요.

예제 입력 & 출력
find_max([1, 3, 7, 2, 5])  # 출력: 7
find_max([-5, -1, -3])  # 출력: -1
find_max([100])  # 출력: 100
find_max([10, 10, 10])  # 출력: 10

"""

def find_max(lst):
    num_max = max(lst)
    print(num_max)

find_max([1, 3, 7, 2, 5])  # 출력: 7
find_max([-5, -1, -3])  # 출력: -1
find_max([100])  # 출력: 100
find_max([10, 10, 10])  # 출력: 10

