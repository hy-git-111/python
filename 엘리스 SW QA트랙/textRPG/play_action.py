# 전투 진행 (fight()) 및 데미지 계산
# 승패 판정 및 경험치 지급 처리
# 

from monster import Monster
from main import GameManager
from ui_manager import Message, Suggestion
from time import sleep

class HuntingManager:

    def met_action(self, user_command, monster, warrior):
        # user_command = input("무엇을 하시겠습니까? (q: 도망가기, h: 사냥하기)")
        if not monster:
            pass
        if user_command == "q":
            Message.run_away_msg()
            return 
        elif user_command == "h":
            self.hunt(monster, warrior)
            if warrior.exp >= 100:
                GameManager.level_up(warrior)

    def hunt(self, monster, warrior):
        Message.hunting_msg()
      
        while monster.hp > 0 and warrior.hp > 0:
            Message.damage_msg(monster, warrior)
            monster.hp -= warrior.ad
            warrior.hp -= monster.ad

            if monster.hp <= 0:
                warrior.exp += monster.exp
                Message.win_msg(monster)
                break
            elif warrior.hp <= 0:
                cmd = Suggestion.lose_suggestion(monster)
                if cmd == "r":
                    self.__init__() # 기존 인스턴스 재설정(인스턴스 초기화)
                    self.start_game()
                elif cmd == "e":
                    return "e"

