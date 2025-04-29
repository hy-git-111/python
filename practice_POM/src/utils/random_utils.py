from resource.product_name import product
import random

class RandomUtils:
    # 랜덤 상품명 반환
    @staticmethod
    def generate_random_product():
        return random.choice(product)
