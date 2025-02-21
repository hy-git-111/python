"""
📌 문제 5: 리스트 중복 제거 (Remove Duplicates in List)
문제 설명
리스트에서 중복된 요소를 제거하고 중복이 없는 리스트를 반환하는 함수를 작성하세요.
출력 리스트는 기존 순서를 유지해야 합니다.

remove_duplicates([1, 2, 2, 3, 4, 4, 5])  # 출력: [1, 2, 3, 4, 5]
remove_duplicates(["a", "b", "a", "c", "b"])  # 출력: ["a", "b", "c"]
remove_duplicates([10, 10, 10, 10])  # 출력: [10]
remove_duplicates([])  # 출력: []
"""

# 방법 1 : for문 사용
def remove_duplicates(lst):
    result_lst = []
    for text in lst:
        if text not in result_lst:
            result_lst.append(text)
    print(result_lst)

# 방법 2 : set() 함수 사용
# def remove_duplicates(lst):
#     result = list(set(lst))
#     print(sort(result))


# 공통 : 함수 실행
remove_duplicates([1, 2, 2, 3, 4, 4, 5])  # 출력: [1, 2, 3, 4, 5]
remove_duplicates(["a", "b", "a", "c", "b"])  # 출력: ["a", "b", "c"]
remove_duplicates([10, 10, 10, 10])  # 출력: [10]
remove_duplicates([])  # 출력: []