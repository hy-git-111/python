# 50명의 승객과 매칭 기회가 있을 때, 총 탑승 승객 수를 구하는 프로그램
# 조건
# 1. 승객별 운행 소요 시간은 5~50분 사이의 난수
# 2. 소요시간 5~15분 사이의 승객만 매칭해야 함
# 3. 출력문 예제
# [O] 1번째 손님 (소요시간 : 15분)
# [ ] 2번째 손님 (소요시간 : 10분)
# 총 탑승객 : 1분
from random import *

customer = range(1,51)
print(list(customer))

time = []
cnt = 0
for i in customer:
    ran = randint(5, 50)
    time.append(ran)
    # print(i)
    if ran >=5 and ran <= 15:
        print(f'[O] {customer[i-1]}번째 손님 (소요시간 : {ran}분)')
        cnt += 1
    else:
        print(f'[ ] {customer[i-1]}번째 손님 (소요시간 : {ran}분)')

print(f'총 탑승객 : {cnt}분')

    
