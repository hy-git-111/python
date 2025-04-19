import sys, os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
import pytest
from palindrome import is_palindrome

# 기본 테스트
normal_params = [
    ("racecar", True),
    ("madam", True),
    ("hello", False),
    ("12321", True),
    ("python", False)
]

capital_params =[
    ("RaceCar", True),
    ("MadAm", True)
]

except_str_params=[
    ("A man, a plan, a canal, Panama", True),
    ("No 'x' in Nixon", True),
    ("Was it a car or a cat I saw?", True)
]

@pytest.mark.parametrize("s, expected", normal_params)
def test_palindrome(s, expected):
    assert is_palindrome(s) == expected

# 대소문자 구분 없이 테스트
@pytest.mark.parametrize("s, expected", capital_params)
def test_capital_palindrome(s, expected):
    assert is_palindrome(s) == expected

# 공백과 특수문자가 포함된 경우 테스트
@pytest.mark.parametrize("s, expected", except_str_params)
def test_except_str(s, expected):
    assert is_palindrome(s) == expected

# 빈 문자열 입력 테스트
def test_blank_str():
    assert is_palindrome("") == True

# 단일 문자 테스트
def test_single_str():
    assert is_palindrome("a") == True

def test_type_err():
    with pytest.raises(TypeError):
        is_palindrome(12345)