# 몬스터 데이터 관리
# 몬스터 생성 관리

import random

class Monster:
    # 몬스터 정보
    monsters = {
    "치타": {"hp": 30, "ad": 5, "speed": 5, "exp": 50}, 
    "고릴라": {"hp": 50, "ad": 5, "speed": 1, "exp": 50},
    "독수리": {"hp": 20, "ad": 5, "speed": 10, "exp": 50}
    }

    # 몬스터 정보를 초기화 하기 위해 클래스 객체 생성
    @ classmethod
    def appeared(cls):
        name_list = list(cls.monsters.keys())
        name = random.choice(name_list)
        monster_data = cls.monsters[name]
        return cls(name, monster_data["hp"], monster_data["ad"], monster_data["speed"], monster_data["exp"])

    # 몬스터 기본 속성 설정
    def __init__(self, name, hp, ad, speed, exp):
        self.name = name
        self.hp = hp
        self.ad = ad
        self.speed = speed
        self.exp = exp
