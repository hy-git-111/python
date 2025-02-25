from monster import Monster
# from main import Operate
from time import sleep

class PlayAction:
    def find_monster(self, warrior):
        sleep(1)
        monster = Monster.appeared()  # 몬스터 랜덤 출몰
    
        print(f"{monster.name}가 나타났다!")
        print(f"{monster.name}의 체력: {monster.hp}, 공격력: {monster.ad}")
        print(f"나의 체력: {warrior.hp}/{warrior.hp_tot}, 공격력: {warrior.ad}, 마나: {warrior.mp}\n")

        user_command = input("무엇을 하시겠습니까? (q: 도망가기, w: 싸우기)")
        if user_command == "q":
            print("잽싸게 도망가기 성공!\n")
        elif user_command == "w":
            self.fight(monster, warrior)
            if warrior.exp >= 100:
                warrior.level(warrior)

    def fight(self, monster, warrior):
        print("싸우기!")
      
        while monster.hp > 0 and warrior.hp > 0:
            print(f"데미지 {warrior.ad}을 주었습니다! ({monster.name}의 체력: {monster.hp})")
            print(f"데미지 {monster.ad}을 받았습니다! (남은 체력: {warrior.hp})")
            monster.hp -= warrior.ad
            warrior.hp -= monster.ad

        if monster.hp == 0 and warrior.hp >= 0:
            warrior.exp += monster.exp
            print(f"{monster.name}을 잡았습니다. 경험치 {monster.exp} 획득!\n")
        else:
            print("패배하였습니다.")
        #     user_command = (f"{monster.name}을 놓쳤습니다. 재 도전 하시겠습니까? (r: 게임 다시 하기, e: 게임 끝내기)")
        #     if user_command == "r":
        #         pass
        #     elif user_command == "e":
        #         return False


