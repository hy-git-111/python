# 표준 체중을 구하는 프로그램

# 공식
# 남자 : 키(m) * 키(m) * 22
# 여자 : 키(m) * 키(m) * 21

# 조건
# 1. 표준 체중은 별도의 함수로 계산
# 2. 표준 체중은 소수점 둘째자리까지 표시
# 3. 출력 예제 : 키 175cm 남자의 표준 체중은 67.38kg 입니다.

def std_weight(height, gender):
    if gender == "남자":
        standardWeight = round((height / 100) ** 2 * 22, 2)
        return standardWeight
        # print(standardWeight)
        # print("키 {0}cm {2}의 표준 체중은 {1}kg 입니다.".format(height, standardWeight, gender))
    else:
        standardWeight = round((height / 100) ** 2 * 21)
        # print("키 {0}cm {2}의 표준 체중은 {1}kg 입니다.".format(height, standardWeight, gender))
        return standardWeight

# std_weight(175, "남자")

height = 175
gender = "남자"
weight = std_weight(height, gender)

print("키 {0}cm {2}의 표준 체중은 {1}kg 입니다.".format(height, weight, gender))

