from character import Character
from play_action import PlayAction
from monster import Monster
from time import sleep
# import random

# 입력값을 통해 동작하는 고전 방식
class Operate:
   def __init__(self):
      self.warrior = Character(100, 100, 0, 5, 1, 0, 1) # hp_tot, hp, mp, ad, lv, exp, speed
      self.action = PlayAction()

   def main(self):
      play = True
      print("게임 시작")
            
   # 게임 실행 및 디스플레이
      while play:
         user_command = input("무엇을 하시겠습니까? (e: 게임 종료, f: 몬스터 찾기, s: 스탯 확인)")

         if user_command == "e":
            print("게임이 종료되었습니다.")
            play = False
         elif user_command == "f":
            self.action.find_monster(self.warrior)
         elif user_command == "s":
            self.warrior.stats(self.warrior)
     
a = Operate()
a.main()