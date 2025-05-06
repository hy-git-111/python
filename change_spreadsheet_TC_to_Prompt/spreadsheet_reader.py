import gspread
from oauth2client.service_account import ServiceAccountCredentials

class GoogleSheetReader:
    scope = [
        "https://spreadsheets.google.com/feeds",
        "https://www.googleapis.com/auth/drive"
    ]

    def __init__(self, creds_file, sheet_name):
        self.creds_file = creds_file
        self.sheet_name = sheet_name

        creds = ServiceAccountCredentials.from_json_keyfile_name(self.creds_file, self.scope)
        
        self.client = gspread.authorize(creds)
        self.sheet = self.get_worksheets()

    # 구글 스프레드 시트에 연결하는 함수
    def get_worksheets(self):
        spreadsheet = self.client.open(self.sheet_name)
        return spreadsheet.worksheets()

    # 전체 데이터를 파이썬 리스트(dict 형식)로 읽어오는 함수 
    def read_test_cases(self):
        return self.sheet.get_all_records(head=2)   # 2행을 헤더로 지정