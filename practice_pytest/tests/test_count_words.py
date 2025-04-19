import pytest
import sys, os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from count_words import count_words

normal_words = [
    ("apple banana apple", {"apple": 2, "banana": 1}),
    ("Python is great and Python is fun", {"python": 2, "is": 2, "great": 1, "and": 1, "fun": 1}),
    ("hello hello hello", {"hello": 3})
]

@pytest.mark.parametrize("text, expected", normal_words)
def test_count_words(text, expected):
    assert count_words(text) == expected


contain_special_words = [
    ("Apple apple APPLE", {"apple": 3}),    # 대소문자 포함 문자열
    ("PYTHON python PyThOn", {"python": 3}),    # 대소문자 포함 문자열
    ("Hello, world! Hello...", {"hello": 2, "world": 1}),   # 특수문자 포함 문자열
    ("Numbers: 123 123 456", {"numbers": 1, "123": 2, "456": 1}),   # 숫자 포함 문자열
    ("single", {"single": 1}),  # 단일 단어 문자열
    ("", {}),    # 공백
    ("The quick brown fox jumps over the lazy dog", {"the": 2, "quick": 1, "brown": 1, "fox": 1, "jumps": 1, "over": 1, "lazy": 1, "dog": 1})   # 긴 문장
]

@pytest.mark.parametrize("text, expected", contain_special_words)
def test_contain_capital(text, expected):
    assert count_words(text) == expected
