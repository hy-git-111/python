# 사이트별로 비밀번호를 만들어 주는 프로그램 작성
# 조건
# 1. url 형식 예시 : https://naver.com/
# 2. http://부분은 제외
# 3. 처음 만나는 점(.)이후 부분은 제외
# 4. 남은 글자 중 처음 세자리 + 글자 갯수 + 글자 내 'e' 갯수 + '!'로 구성

url = "https://naver.com/"

string = url.replace("https://", "")
# print(string)

findDot = string.find(".")
# print(findtDot)
string = str(string[:findDot])
# print(string)

cntE = str(string.count('e'))
password = string[:3] + str(len(string)) + cntE + "!"
print(password)