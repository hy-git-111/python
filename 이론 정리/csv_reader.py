import csv

with open("data.csv", "r", encoding="utf-8") as f:  # data.csv를 r모드로 열기
    reader = csv.reader(f)  # csv 파일을 작성하는 reader 객체 생성 
    for row in reader:
        print(row)