import sys, os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from fibonacci import fibonacci, fibonacci_recursive
import pytest


normal_fibonacci = [
    (0, 0),
    (1, 1),
    (2, 1),
    (3, 2),
    (4, 3),
    (5, 5),
    (10, 55),
    (15, 610)
]

except_fibonacci = [-1, "5", 3.5, None]

big_number_fibonacci = [
    (50, 12586269025),
    (100, 354224848179261915075)
]

@pytest.mark.parametrize("n, expected", normal_fibonacci)
def test_normal_fibonacci(n, expected):
    assert fibonacci(n) == expected

@pytest.mark.parametrize("n", except_fibonacci)
def test_except_fibonacci(n):
    with pytest.raises(ValueError, match="n은 0 이상의 정수여야 합니다."):
        fibonacci(n)

@pytest.mark.parametrize("n, expected", big_number_fibonacci)
def test_big_number_fibonacci(n, expected):
    assert fibonacci(n) == expected

@pytest.mark.parametrize("n, expected", normal_fibonacci)
def test_normal_fibonacci_recursive(n, expected):
    assert fibonacci_recursive(n) == expected

@pytest.mark.parametrize("n", except_fibonacci)
def test_except_fibonacci_recursive(n):
    with pytest.raises(ValueError, match="n은 0 이상의 정수여야 합니다."):
        fibonacci_recursive(n)

@pytest.mark.parametrize("n, expected", big_number_fibonacci)
def test_big_number_fibonacci_recursive(n, expected):
    assert fibonacci_recursive(n) == expected


