# 플레이어 데이터 관리
# 스탯 관련 로직 관리

# from time import sleep

class Character:
    def __init__(self, hp_tot, hp, mp, ad, lv, exp, speed):
        self.hp_tot = hp_tot
        self.hp = hp
        self.mp = mp
        self.ad = ad
        self.lv = lv
        self.exp = exp
        self.speed = speed
    
    def stats(warrior):
        print("_" * 50)
        print(f"레벨: {warrior.lv}, 경험치: {warrior.exp}, 마나: {warrior.mp}")
        print(f"체력: {warrior.hp}/{warrior.hp_tot}, 공격력: {warrior.ad}, 공격 속도{warrior.speed}")
        print("_" * 50)
        print()

    
        


