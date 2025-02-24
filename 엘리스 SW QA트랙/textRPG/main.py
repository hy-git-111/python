# HP : health point
# AD : attack damage
# MP : mana point

from character import Character
from monster import Monster

# 입력값을 통해 동작하는 고전 방식
class Operate:
   def __init__(self):
      self.warrior = Character(100, 0, 5)

   def main(self):
      print("게임 시작")
            
   # 게임 실행 및 디스플레이
      while True:
         user_command = input("무엇을 하시겠습니까? (e: 게임 종료, f: 몬스터 찾기)")

         if user_command == "e":
            print("게임이 종료되었습니다.")
            break
         elif user_command == "f":
            self.action(self.warrior)

   def action(self, warrior):
      monster = Monster("고릴라", 10, 1)

      print(f"{monster.name}가 나타났다!")
      print(f"{monster.name}의 체력: {monster.hp}, 공격력: {monster.ad}")
      print(f"나의 체력: {warrior.hp}, 마나: {warrior.mp}, 공격력: {warrior.ad}\n")

      user_command = input("무엇을 하시겠습니까? (q: 도망가기, w: 싸우기)")

      if user_command == "q":
         print("잽싸게 도망가기 성공!\n")
      elif user_command == "w":
         self.fight(monster, self.warrior)
   
   def fight(self, monster, warrior):
      print("싸우기!")
      while monster.hp > 0 and warrior.hp > 0:
         monster.hp -= warrior.ad
         print(f"{monster.name}의 체력: {monster.hp}")
         warrior.hp -= monster.ad
         print(f"나의 체력: {warrior.hp}")
      
      if monster.hp == 0:
         print(f"{monster.name}가 죽었습니다.\n")
         return
      else:
            print(f"패배하였습니다.\n")
            return
     
a = Operate()
a.main()