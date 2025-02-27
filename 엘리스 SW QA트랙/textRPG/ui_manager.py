# 입력 (input()) 및 출력 (print()) 처리

class Message:
    # 유효한 스탯 명령어 정리
    stats_cmds = {
        "h": "최대 체력",
        # "d": "공격 데미지",
        # "s": "공격 속도"
        }
    
    # 유효한 게임 실행 명령어 정리
    play_cmds = {
        "e": "게임 종료", 
        "f": "몬스터 찾기",
        "s": "스탯 확인",
        "r": "게임 다시 시작",
        "q": "도망가기", 
        "h": "사냥하기"
        }

    # 플레이어 스탯 표시
    def stats(warrior):
        print("_" * 50)
        print(f"레벨: {warrior.lv}, 경험치: {warrior.exp}, 마나: {warrior.mp}")
        print(f"체력: {warrior.hp}/{warrior.hp_tot}, 공격력: {warrior.ad}, 공격 속도{warrior.speed}")
        print("_" * 50)
        print()

    # 몬스터가 나타났을 때 출력 메세지
    def appeared_msg(monster, warrior):
        print(f"{monster.name}(을/를) 발견했다!")
        print(f"{monster.name}의 체력: {monster.hp}, 공격력: {monster.ad}")
        print(f"나의 체력: {warrior.hp}/{warrior.hp_tot}, 공격력: {warrior.ad}, 마나: {warrior.mp}\n")

    # 사냥할 때 출력 메세지
    def damage_msg(monster, warrior):
        print(f"데미지 {warrior.ad}을 주었습니다! ({monster.name}의 체력: {monster.hp})")
        print(f"데미지 {monster.ad}을 받았습니다! (남은 체력: {warrior.hp})")

    # 사냥 성공 시 출력 메세지
    def win_msg(monster):
        print(f"{monster.name}을 잡았습니다. 경험치 {monster.exp} 획득!")

    # 사냥 성공하여 스텟 올릴때 출력 메세지
    @staticmethod
    def stat_up_msg(cmd, value):
        print(f"{Message.stats_cmds[cmd]} (이/가) {value} 증가하였습니다.")

    # 게임 실행 명령어 입력 후, 입력한 명령어가 제대로 실행되는지 사용자가 확인하기 위한 출력 메세지
    @staticmethod
    def game_action_msg(cmd):
        Message.play_cmds[cmd]
        print(f"{Message.play_cmds[cmd]}\n")

    # 명령어를 잘못 입력한 경우 출력 메세지
    @staticmethod
    def not_allowed_cmd_msg():
        print("잘못된 입력입니다. 올바른 명령어를 입력하세요.")

    # 게임 시작 시 출력 메세지
    @staticmethod
    def start_game_msg():
        print("게임 시작")

    # 도망가기 시 출력 메세지
    @staticmethod
    def run_away_msg():
        print("잽싸게 도망가기 성공!")

    # 레벨 업 시 출력 메세지
    @staticmethod
    def level_up_msg():
        print("경험치가 가득 찼습니다. 레벨 업!")

    # 사냥 실패 후 게임 재 실행 시 출력 메세지
    @staticmethod
    def revival_msg():
        print("부활!")


class Suggestion:
    def lose_suggestion(monster):
        cmd = input(f"\n{monster.name}을 놓쳤습니다. 재 도전 하시겠습니까? (r: 게임 다시 하기, e: 게임 끝내기)")
        return cmd
    
    @staticmethod
    def play_suggestion():
        cmd = input("\n무엇을 하시겠습니까? (e: 게임 종료, f: 몬스터 찾기, s: 스탯 확인)")
        return cmd

    @staticmethod
    def met_monster_suggestion():
        cmd = input(f"\n무엇을 하시겠습니까? (q: 도망가기, h:사냥하기)")
        return cmd

    @staticmethod
    def level_up_suggestion():
        cmd = input(f"\n어떤 능력치를 강화할까요? (h: 최대 체력)")
        # cmd = input(f"어떤 능력치를 강화할까요? (h: 최대 체력, d: 공격 데미지 s: 공격 속도)")
        return cmd

class Validation:
    # 유효성 평가용 플레이 cmd 정리
    @staticmethod
    def allowed_play_cmds(context):
        cmds = {
            "game_start": {"e", "f", "s"},
            "met_monster": {"q", "h"},
            "lose": {"r", "e"}
        }
        return cmds.get(context, set())
    
    # 유효성 평가용 스텟 업데이트 cmd 정리
    @staticmethod
    def allowed_stats_cmds(context):
        cmds = {
            "stat_up": {"h", "d", "s"}
        }
        return cmds.get(context, set())
    
    # 플레이 cmd 유효성 평가 로직
    @staticmethod
    def validation_play_cmd(cmd, context):
      allowed_play_cmds = Validation.allowed_play_cmds(context)
      return cmd in allowed_play_cmds
    
    # 스텟 업데이트 cmd 유효성 평가 로직
    @staticmethod
    def validation_stats_cmd(cmd, context):
      allowed_play_cmds = Validation.allowed_stats_cmds(context)
      return cmd in allowed_play_cmds

