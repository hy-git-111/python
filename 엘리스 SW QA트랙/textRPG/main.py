# 게임 전체 진행 및 흐름 관리
# 플레이어 입력을 받아 액션 수행 (전투, 몬스터 탐색 등)
# Operate > GameManager

from character import Character
from play_action import HuntingManager
from monster import Monster
from ui_manager import Suggestion, Message
from time import sleep
# import random

# 입력값을 통해 동작하는 고전 방식
class GameManager:
   def level_up(self, warrior):
         warrior.lv += 1
         warrior.exp = 0
         value = 1 * warrior.lv

         Message.level_up_msg()  # print("경험치가 가득 찼습니다. 레벨 업!")
         cmd = Suggestion.level_up_suggestion() # level_up_cmd = input("어떤 능력치를 강화할까요? (h: 최대 체력, d: 공격 데미지 s: 공격 속도)")  
         
         if cmd in Message.stats_cmd:
            warrior.hp_tot += value
            Message.stat_up_msg(cmd, value)
            return

   def find_monster(self, warrior):
      sleep(1)
      monster = Monster.appeared()  # 몬스터 랜덤 출몰
      Message.appeared_msg(monster, warrior) # print(f"{monster.name}을/를 발견했다!")
      return monster
      
   def start_game(self):
      Message.start_game_msg()
   # 게임 실행 및 디스플레이
      while True:
         
         default_cmd = Suggestion.play_suggestion()
         print(default_cmd)
         # cmd = input("무엇을 하시겠습니까? (e: 게임 종료, f: 몬스터 찾기, s: 스탯 확인)")
         Message.game_action(default_cmd)
         if default_cmd == "e":
            break
         elif default_cmd == "f":
            monster = self.find_monster(self.warrior)
            suggestion_cmd = Suggestion.met_monster_suggestion()
            self.hunt.met_action(suggestion_cmd, monster, self.warrior)
         elif default_cmd == "s":
            Character.stats(self.warrior)

   def __init__(self):
      self.warrior = Character(100, 100, 0, 5, 1, 0, 1) # hp_tot, hp, mp, ad, lv, exp, speed
      self.hunt = HuntingManager()

a = GameManager()
a.start_game()