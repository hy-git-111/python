# 댓글 작성자들 중에 추첨을 통해 1명은 치킨, 3명은 커피 쿠폰을 받는 프로그램을 작성한다.
# 조건
# 1. 댓글은 20명이 작성하였고, 아이디는 1~20이라고 가정
# 2. 댓글 내용과 상관 없이 무작위로 추첨하되 중복 불가
# 3. random 모듈의 shuffle과 sample 활용
from random import *

idList = []

for i in range(20):
    idList.append(i+1)
# print(idList)

shuffle(idList)
result = sample(idList, 4)
# print(result)

print(f'커피 당첨자는 {result[0]}')
print(f'치킨 당첨자는 {result[1:]}')