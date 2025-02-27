# 플레이어 데이터 관리
# 스탯 관련 로직 관리 < 기간 내 분리 못함

class Character:
    # 플레이어 기본값 설정
    def __init__(self, hp_tot, hp, mp, ad, lv, exp, speed):
        self.hp_tot = hp_tot
        self.hp = hp
        self.mp = mp
        self.ad = ad
        self.lv = lv
        self.exp = exp
        self.speed = speed

    
        


