# 입력 (input()) 및 출력 (print()) 처리
class Message:
    stats_cmds = {
        "h": "최대 체력",
        "d": "공격 데미지",
        "s": "공격 속도"
        }

    play_cmds = {
        "e": "게임 종료", 
        "f": "몬스터 찾기",
        "s": "스탯 확인",
        "r": "게임 다시 시작",
        "q": "도망가기", 
        "h": "사냥하기"
        }

    def appeared_msg(monster, warrior):
        print(f"{monster.name}을/를 발견했다!")
        print(f"{monster.name}의 체력: {monster.hp}, 공격력: {monster.ad}")
        print(f"나의 체력: {warrior.hp}/{warrior.hp_tot}, 공격력: {warrior.ad}, 마나: {warrior.mp}\n")
    
    def damage_msg(monster, warrior):
        print(f"데미지 {warrior.ad}을 주었습니다! ({monster.name}의 체력: {monster.hp})")
        print(f"데미지 {monster.ad}을 받았습니다! (남은 체력: {warrior.hp})")

    def win_msg(monster):
        print(f"{monster.name}을 잡았습니다. 경험치 {monster.exp} 획득!\n")

    def stat_up_msg(self, cmd, value):
        print(f"{self.stats_cmds[cmd]} 이/가 {value} 증가하였습니다. ({self.stats_cmds[cmd]}: {self.stats_cmds.values[cmd]})")
    
    @staticmethod
    def game_action(cmd):
        print(f"{Message.play_cmds[cmd]}")

    @staticmethod
    def start_game_msg():
        print("게임 시작")

    @staticmethod
    def run_away_msg():
        print("잽싸게 도망가기 성공!\n")

    @staticmethod
    def hunting_msg():
        print("사냥하기!")

    @staticmethod
    def level_up_msg():
        print("경험치가 가득 찼습니다. 레벨 업!")
    
    # @staticmethod
    # def lose_msg():
    #     print("패배하였습니다.")


class Suggestion:
    def lose_suggestion(monster):
        cmd = (f"{monster.name}을 놓쳤습니다. 재 도전 하시겠습니까? (r: 게임 다시 하기, e: 게임 끝내기)")
        return cmd
    
    @staticmethod
    def play_suggestion():
        cmd = input("무엇을 하시겠습니까? (e: 게임 종료, f: 몬스터 찾기, s: 스탯 확인)")
        return cmd

    @staticmethod
    def met_monster_suggestion():
        cmd = input(f"무엇을 하시겠습니까? (q: 도망가기, h:사냥하기)")
        return cmd

    @staticmethod
    def level_up_suggestion(stats_cmds):
        cmd = input(f"어떤 능력치를 강화할까요? {stats_cmds}")
        return cmd

# Suggestion.play_suggestion()