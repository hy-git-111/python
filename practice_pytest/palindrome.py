# 회문인지 확인하는 코드
def is_palindrome(s):
    # clean_s = "".join(c.lower() for c  in s if c.isalnum())
    # return clean_s == clean_s[::-1]

    # 1. 문자열에서 영숫자(알파벳과 숫자)만 남기기
    filtered_chars = []
    for c in s:
        if c.isalnum():  # 영숫자인 경우만 추가
            filtered_chars.append(c.lower())  # 소문자로 변환하여 추가
    
    # 2. 리스트를 문자열로 변환
    clean_s = "".join(filtered_chars)

    # 3. 회문 판별 (앞뒤가 같은지 비교)
    return clean_s == clean_s[::-1]