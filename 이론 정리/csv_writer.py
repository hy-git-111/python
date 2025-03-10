import csv

gildong_families = [
    ["ttochi", "dul-li", "Heedong"],
    ["duck", "dinosaur", "person"]
    ]   # 2차원 리스트 형태(2행 3열)

with open("data.csv", "w", encoding="utf-8") as f:  # data.csv를 w모드로 열기(내용 없음)
    writer = csv.writer(f)  # csv 파일을 작성하는 writer 객체 생성 
    writer.writerows(gildong_families)  # 리스트의 리스트를 한번에 기록(저장)