흐름
- 구글 Spread sheets API 연동하여 데이터 추출
- 추출한 데이터 프롬프트 형식으로 변경
- OpenAI API 연동하여 프롬프트 전달

1. 구글 스프레드시트 API 사용 설정
[참고 링크 : IT만물상 Google Sheet 사용 (credentials.json)](https://posbar.tistory.com/260)


2. 라이브러리 설치
- gspread 라이브러리  
: Google Sheets와 Python을 연결해주는 대표 라이브러리

- ServiceAccountCredentials  
: Google API 인증을 위한 라이브러리  

```
pip install gspread oauth2client
```

3. 