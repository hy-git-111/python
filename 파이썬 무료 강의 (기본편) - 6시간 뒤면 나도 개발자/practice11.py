# 퀴즈9
# 치킨집 자동 주문 시스템의 시스템 코드를 확인하고 적절한 예외처리 구문을 넣기

# 조건
# 1. 입력값이 1보다 작거나 숫자가 아닌 입력값이 들어올 때는 ValueError로 처리
# 출력 메세지 : "잘못된 값을 입력하였습니다."
# 2. 대기 손님이 주문할 수 있는 총 치킨량은 10마리
# 치킨 소진 시 사용자 정의 에러[SoldOutError]를 발생시키고 프로그램 종료
# 출력 메세지 : "재고가 소진되어 더 이상 주문을 받지 않습니다."

class ValueRangeError(Exception):
    pass

class SoldOutError(Exception):
    pass



chicken = 10
waiting = 1
status = True

while(status):
    try:
        print("[남은 치킨 : {0}]".format(chicken))
        order = int(input("치킨을 몇마리 주문하시겠습니까?"))
        if order > chicken:
            print("재료가 부족합니다.")
        elif order <= 0:
            raise ValueRangeError
        else:
            print("[대기번호 {0}] {1}마리 주문이 완료되었습니다.".format(waiting, order))
            waiting += 1
            chicken -= order
            
        if chicken == 0:
            raise SoldOutError
    except ValueError:
        print("잘못된 값을 입력하였습니다.")
    except ValueRangeError:
        print("잘못된 값을 입력하였습니다.")
    except SoldOutError:
        status = False
        print(" 재고가 소진되어 더 이상 주문을 받지 않습니다.")