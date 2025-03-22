# pytest tests/test_movie.py

import sys, os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

import pytest
from calculate import add, minus, multiply, divide

add_valid_params = [
    (2, 3, 5),
    (-1, 1, 0),
    (0, 0, 0),
    (100, 200, 300),
    ]

minus_valid_params = [
    (3, 2, 1),
    (-1, 1, -2),
    (0, 0, 0),
    (100, 200, -100),
    ]

add_minus_invalid_params = [
    ("2", 3, TypeError),
    ("", 3, TypeError)
]

multiply_valid_params = [
    (2, 3, 6),
    (-1, 5, -5),
    (0, 10, 0),
    (7, 7, 49),
    (100, 0, 0)
]

div_valid_params = [
    (10, 2, 5.0),
    (-6, 3, -2.0),
    (0, 5, 0.0), 
    (7, 2, 3.5)
]

@pytest.mark.parametrize("a, b, expected", add_valid_params)
def test_add(a, b, expected):
    assert add(a, b) == expected

@pytest.mark.parametrize("a, b, expected_exception", add_minus_invalid_params)
def test_add_type_err(a, b, expected_exception):
    with pytest.raises(expected_exception):
        add(a, b)

@pytest.mark.parametrize("a, b, expected", minus_valid_params)
def test_minus(a, b, expected):
    assert minus(a, b) == expected

@pytest.mark.parametrize("a, b, expected_exception", add_minus_invalid_params)
def test_minus_type_err(a, b, expected_exception):
    with pytest.raises(expected_exception):
        minus(a, b)

@pytest.mark.parametrize("a, b, expected", multiply_valid_params)
def test_multiply(a, b, expected):
    assert multiply(a, b) == expected

def test_multiply_exception():
    with pytest.raises(TypeError, match="Type Error 발생"):
        multiply("a", 3)

@pytest.mark.parametrize("a, b, expected", div_valid_params)
def test_div(a, b, expected):
    assert divide(a, b) == expected

def test_invalid_div():
    with pytest.raises(ZeroDivisionError, match="0으로 나눌 수 없습니다."):
        divide(5, 0)

def test_float_div():
    with pytest.raises(TypeError):
        divide(10, "2")