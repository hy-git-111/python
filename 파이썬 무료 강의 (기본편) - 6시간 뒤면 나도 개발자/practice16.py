# 모듈 호출
# import practice16_module   # 불러올 모듈은 동일 경로 또는 라이브러리 폴더에 있어야 함

# practice16_module.price(3)
# practice16_module.price_morning(2)
# practice16_module.price_solder(5)


# 별칭으로 모듈 호출
# import practice16_module as mv

# mv.price(3)
# mv.price_morning(2)
# mv.price_solder(5)


# from import문 : 모듈명 없이 함수 호출
# from practice16_module import *

# price(3)
# price_morning(2)
# price_solder(5)



# from import문 : 모듈명 없이 원하는 함수만 호출
from practice16_module import price, price_morning

price(3)
price_morning(2)

