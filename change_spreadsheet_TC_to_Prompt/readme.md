흐름
- 구글 Spread sheets API 연동하여 데이터 추출
- 추출한 데이터 프롬프트 형식으로 변경
- OpenAI API 연동하여 프롬프트 전달

1. 구글 스프레드시트 API 사용 설정
[참고 링크 : IT만물상 - Google Sheet 사용 (credentials.json)](https://posbar.tistory.com/260)


2. 라이브러리 설치
- gspread 라이브러리  
: Google Sheets와 Python을 연결해주는 대표 라이브러리

- ServiceAccountCredentials  
: Google API 인증을 위한 라이브러리  

```
pip install gspread oauth2client
```

3. claude 사용을 위한 설정
[참고 링크 : kim90 - 클로드(Claude)와 함께하는 첫 걸음 빠른 시작 가이드] (https://kim90story.tistory.com/215)
- 가상환경 활성화
- 라이브러리 설치
```
pip install anthropic
```
- 환경변수 추가
ANTHROPIC_API_KEY / api키
- api 키 설정
```
setx ANTHROPIC_API_KEY "your-api-key-here"
```
- 현재 터미널에 api 키 적용
```
$env:ANTHROPIC_API_KEY="your-api-key-here"
```