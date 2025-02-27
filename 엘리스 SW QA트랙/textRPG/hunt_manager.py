# 사냥 및 데미지 계산
# 승패 판정 및 경험치 지급 처리

from ui_manager import Message, Suggestion
from ui_manager import Validation
import time
import sys

class HuntManager:
    # monster를 만났을때
    def met_action(self, user_command, monster, warrior, game_manager):       
        if not monster:
            return
        if user_command == "q":
            Message.run_away_msg()
            return 
        elif user_command == "h":
            self.hunt(user_command, monster, warrior, game_manager)

    # monster 사냥 시작
    def hunt(self, cmd, monster, warrior, game_manager):
        Message.game_action_msg(cmd)
        time.sleep(1)
      
        while monster.hp > 0 and warrior.hp > 0:
            monster.hp -= warrior.ad
            warrior.hp -= monster.ad
            Message.damage_msg(monster, warrior)

            if warrior.hp <= 0: # 플레이어가 진 경우
                cmd = Suggestion.lose_suggestion(monster)

                while not Validation.validation_play_cmd(cmd, "lose"):   # cmd 입력값 유효성 검사
                    Message.not_allowed_cmd_msg()
                    cmd = Suggestion.lose_suggestion(monster)
                      
                if cmd == "r":  # 게임 다시 실행
                    Message.revival_msg()
                    game_manager.restart_game()
                    return
                
                elif cmd == "e":    # 게임 종료
                    Message.game_action_msg(cmd)
                    sys.exit()
                
            if monster.hp <= 0: # 플레이어가 이긴 경우
                warrior.exp += monster.exp
                Message.win_msg(monster)

                if warrior.exp >= 100:
                    game_manager.level_up(warrior)
                break
