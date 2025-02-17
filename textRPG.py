import os
import time
import json
import threading

class TycoonGame:
    def __init__(self):
        self.money = 0
        self.income_per_sec = 1
        self.upgrade_cost = 10
        self.running = True
        self.last_play_time = time.time()   # 현재 시간 저장
        self.save_dir = r"D:\Hyeyoung\python\python\TextRPG"    # 저장할 폴더 경로
        self.save_path = os.path.join(self.save_dir, "gameData.json")   # 저장할 파일 경로
        
        self.load_game()
        self.offline_income()

# 게임 데이터 불러오기
    def load_game(self):
        # print("현재 실행 중인 스크립트의 경로u:", os.getcwd())
        if os.path.exists(self.save_path):
            with open(self.save_path, "r") as f:  # 자원을 획득 > 사용 후 반납해야 하는 경우 with문 사용
                data = json.load(f)     # json : dict, list 등 기본 타입만 저장 및 반환 / 객체 저장 및 반환 시 pickle 사용
                self.money = data["money"]
                self.income_per_sec = data["upgrade_cost"]
                self.last_play_time = data.get("last_play_time", time.time())   # 없으면 현재 시간 사용
            print("게임 데이터 불러오기 완료")            

# 게임 데이터 저장하기
    def save_game(self):
        data = {
            "money": self.money,
            "income_per_sec": self.income_per_sec,
            "upgrade_cost": self.upgrade_cost,
            "last_play_time": time.time()
        }

        if not os.path.exists(self.save_dir):
            os.makedirs(self.save_dir)

            with open(self.save_path, "w") as f:
                json.dump(data, f)
                print("게임 저장 완료 ({self.save_path})")

# 돈 자동 적립
    def earn_money(self):
        while self.running:     # 무한루프
            self.money += self.income_per_sec
            print(f"현재 보유 금액 : {self.money}원")
            time.sleep(1)       # 1초마다 수입 증가

# 수입 업그레이드
    def upgrade(self):
        if self.money >= self.upgrade_cost:
            self.money -= self.upgrade_cost
            self.income_per_sec += 1
            self.upgrade_cost *= 2
            print(f"업그레이드 완료! 현재 초당 수입 : {self.income_per_sec}원")
            self.save_game()    # 업그레이드 후 자동 저장
        else:
            print("현재 보유 금액이 부족합니다.")

# 오프라인 수익 계산
    def offline_income(self):
        current_time = time.time()
        elapsed_time = int(current_time - self.last_play_time)  # 지난 시간 계산
        offline_earnings = int(elapsed_time * self.income_per_sec)
        self.money += offline_earnings
        print(f"오프라인 수익 지급: {offline_earnings}원 (경과 시간: {elapsed_time})")

# 자동 실행을 위한 스레드 실행
    def start(self):
        self.running = True # 게임 실행 상태 유지
        earn_thread = threading.Thread(target=self.earn_money)  # 스레드 생성, target이 별도의 스레드에서 실행
        earn_thread.daemon = True   # 메인 프로그램 종료 시 자동 종료
        earn_thread.start() # 생성한 새 스레드 실행

    def stop(self):
        self.running = False
        self.save_game()
        print("백그라운드 실행 종료")

game = TycoonGame()
game.start()

while True:
    command = input("명령어를 입력하세요 (u: 업그레이드, q: 종료, qq: 완전 종료): ")
    if command.lower() == "u":
        game.upgrade()
    elif command.lower() == "q":
        print("게임 종료, 백그라운드 실행 유지")
        game.save_game()
        break
    elif command.lower() == "qq":
        print("게임 종료, 백그라운드 실행 종료")
        game.save_game()
        break
