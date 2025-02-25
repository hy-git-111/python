# from monster import monsters
from time import sleep

class Character:
    def __init__(self, hp_tot, hp, mp, ad, lv, exp, speed):
        self.hp_tot = hp_tot
        self.hp = hp
        self.mp = mp
        self.ad = ad
        self.lv = lv
        self.exp = exp
        self.speed = speed
    
    def stats(self, warrior):
        print("_" * 50)
        print(f"레벨: {warrior.lv}, 경험치: {warrior.exp}, 마나: {warrior.mp}")
        print(f"체력: {warrior.hp}/{warrior.hp_tot}, 공격력: {warrior.ad}, 공격 속도{warrior.speed}")
        print("_" * 50)
        print()

    def level(self, warrior):
        warrior.lv += 1
        warrior.exp = 0
        print("경험치가 가득 찼습니다. 레벨 업!")
        user_command = input("어떤 능력치를 강화할까요? (h: 최대 체력, d: 공격 데미지 s: 공격 속도)")  
    
        if user_command == "h":
            warrior.hp_tot += 10
            print(f"최대 체력이 10 증가하였습니다.(체력: {warrior.hp}/{warrior.hp_tot})\n")
            return
        elif user_command == "d":
            warrior.ad += 1
            print(f"공격력이 1 증가하였습니다.(공격력: {warrior.ad})\n")
            return
        elif user_command == "s":
            warrior.speed += 1
            print(f"공격 속도가 1 증가하였습니다.(공격 속도: {warrior.speed})\n")
            return
        


