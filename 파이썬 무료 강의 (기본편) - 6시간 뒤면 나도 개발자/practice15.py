class RangeError(Exception):
    def __init__(self, msg):
        self.msg = msg
    
    def __str__(self):
        return self.msg
    


try:
    print("한자리 숫자 나누기 전용 계산기입니다.")
    n1 = int(input("첫 번째 숫자를 입력하세요. : "))
    n2 = int(input("두 번째 숫자를 입력하세요. : "))
    if  n1 >= 10 or n2 >= 10:
        raise RangeError("입력값 : {0}, {1}".format(n1, n2))
    print("{0} / {1} = {2}".format(n1, n1, int(n1 / n2)))

except ValueError:
    print("잘못된 값을 입력하였습니다.")
except RangeError as e:
    print("잘못된 값을 입력하였습니다.")
    print(e)
finally:
    print("계산기를 종료합니다.")