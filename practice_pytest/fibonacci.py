def fibonacci(n: int) -> int:
    if not isinstance(n, int) or n < 0:
        raise ValueError("n은 0 이상의 정수여야 합니다.")
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b
    
def fibonacci_recursive(n: int) -> int:
    if not isinstance(n, int) or n <0:
        raise ValueError("n은 0 이상의 정수여야 합니다.")
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)
