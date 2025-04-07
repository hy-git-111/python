# https://support.google.com/mail/answer/7126229?hl=ko
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

# 사용자 정보 입력
sendEmail = "@gmail.com"
recvEmail = "@gmail.com"
password = "1234"

# SMTP 서버 정보 설정
smtpName = "smtp.gmail.com"
smtpPort = 587

# 여러 MIME을 넣기 위한 MIMEMultipart 객체 생성
msg = MIMEMultipart()

# MIME 객체 생성
text = "메일 내용"
contentPart = MIMEText(text, "plain", "utf-8")
msg.attach(contentPart)

# 파일 추가
etcFileName = 'C:\Users\a\Desktop\구름.jpg  '
with open(etcFileName, 'rb') as etcFD:  # 첨부파일을 read binary
    etcPart = MIMEApplication(etcFD.read())
    etcPart.add_header('Content-Disposition', 'attachment', filename=etcFileName)   # 첨부 파일의 정보 추가
    msg.attach(etcPart)

# MIME 헤더 설정
msg['Subject'] = "메일 제목"
msg['From'] = sendEmail
msg['To'] = recvEmail
print(msg.as_string())  # 텍스트 형식으로 전송

# SMTP 서버 연결
s = smtplib.SMTP(smtpName, smtpPort)
s.starttls()    # start TLS
s.login(sendEmail, password)    # SMTP 서버에 로그인
s.sendmail(sendEmail, recvEmail, msg.as_string())   # 문자열로 변환하여 메일 전송
s.close()   # 서버 연결 종료