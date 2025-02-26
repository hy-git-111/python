# 몬스터 데이터 관리
# 몬스터 생성 관리
import random

class Monster:
    monsters = {
    "고릴라": {"hp": 80, "ad": 2, "speed": 1, "exp": 60},
    "치타": {"hp": 80, "ad": 1, "speed": 5, "exp": 60}, 
    # "독수리": {"hp": 30, "ad": 5, "speed": 10, "exp": 10}
    }

    # 몬스터 정보를 초기화 하기 위해 클래스 객체 생성
    @ classmethod
    def appeared(cls):
        name_list = list(cls.monsters.keys())
        name = random.choice(name_list)
        monster_data = cls.monsters[name]
        
        return cls(name, monster_data["hp"], monster_data["ad"], monster_data["speed"], monster_data["exp"])

    def __init__(self, name, hp, ad, speed, exp):
        self.name = name
        self.hp = hp
        self.ad = ad
        self.speed = speed
        self.exp = exp
# 레벨별 출몰 데이터 추가
# print(Monster.appeared())