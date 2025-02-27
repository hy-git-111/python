# 게임 전체 진행 및 흐름 관리

from character import Character
from hunt_manager import HuntManager
from monster import Monster
from ui_manager import Suggestion, Message, Validation
from time import sleep
import sys


class GameManager:
   # 레벨 업
   def level_up(self, warrior):
         warrior.lv += 1
         warrior.exp = 0
         value = 1 * warrior.lv

         Message.level_up_msg()
         cmd = Suggestion.level_up_suggestion()
         while not Validation.validation_stats_cmd(cmd, "stat_up"):
               Message.not_allowed_cmd_msg()
               cmd = Suggestion.level_up_suggestion()

         if cmd in Message.stats_cmds: # 사용자 최대 체력 강화 로직
            warrior.hp_tot += value
            Message.stat_up_msg(cmd, value)
            return
         
   # 몬스터 찾기
   def find_monster(self, warrior):
      sleep(1)
      monster = Monster.appeared()  # 몬스터 랜덤 출몰 함수 호출
      Message.appeared_msg(monster, warrior)
      return monster
   
   # 게임 실행
   def start_game(self):
      Message.start_game_msg()
      self.warrior = Character(100, 100, 0, 5, 1, 0, 1)

      while True:
         default_cmd = Suggestion.play_suggestion()

         if not Validation.validation_play_cmd(default_cmd, "game_start"):
            Message.not_allowed_cmd_msg()
            continue
         Message.game_action_msg(default_cmd)

         if default_cmd == "e":
            sys.exit()

         elif default_cmd == "f":
            monster = self.find_monster(self.warrior)
            suggestion_cmd = Suggestion.met_monster_suggestion()

            while not Validation.validation_play_cmd(suggestion_cmd, "met_monster"):
               Message.not_allowed_cmd_msg()
               suggestion_cmd = Suggestion.met_monster_suggestion()
               
            hunt_manager = HuntManager()  # 순환 종속성 방지
            hunt_manager.met_action(suggestion_cmd, monster, self.warrior, self)
         
         elif default_cmd == "s":
            Message.stats(self.warrior)

   # 게임 재 실행
   def restart_game(self):
      self.warrior = Character(100, 100, 0, 5, 1, 0, 1)
      self.start_game()

# 게임 시작 함수 호출
a = GameManager()
a.start_game()