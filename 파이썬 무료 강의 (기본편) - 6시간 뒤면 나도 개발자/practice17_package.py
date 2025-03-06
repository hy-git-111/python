# import는 패키지, 모듈만 불러올 수 있음
# import travel.thailand  
# trip_to = travel.thailand.ThilandPackage()
# trip_to.detail()


# from import는 패키지, 모듈, 함수 보두 불러올 수 있음
# from travel.thailand import ThilandPackage  
# trip_to = ThilandPackage()
# trip_to.detail()


# from travel import vietnam
# trip_to = vietnam.VietnamPackage()
# trip_to.detail()


# __init__폴더에서 공개 범위 설정
from travel import *
trip_to = vietnam.VietnamPackage()
trip_to.detail()
trip_to = thailand.ThilandPackage()
trip_to.detail()


# 모듈의 위치 확인하기
import inspect
import travel
print(inspect.getfile(travel))