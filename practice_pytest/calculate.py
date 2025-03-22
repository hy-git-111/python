# 덧셈 함수
def add(a: int, b: int) -> int:
    return a + b

# 뺄셈 함수
def minus(a: int, b: int) -> int:
    return a - b

# 곱셈 함수
def multiply(a: int, b: int) -> int:
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("Type Error 발생")
    return a * b

# 나눗셈 함수
def divide(a: int, b: int) -> float:
    if b == 0:
        raise ZeroDivisionError("0으로 나눌 수 없습니다.")
    return a / b