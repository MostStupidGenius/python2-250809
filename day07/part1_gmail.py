# part1_gmail.py
# 파이썬을 이용하여 SMTP를 알고 그 라이브러리로 
# Gmail을 보낼 수 있다.
# SMTP(Simple Mail Transfer Protocol)
# 간단하게 이메일을 보낼 수 있도록 정해놓은 전달 규칙(프로토콜)
# 라이브러리 smtplib가 필요하다
import smtplib # 파이썬에서 기본으로 설치되기 때문에
# 추가적인 설치는 필요없다
# smtp는 메일을 보내기 위한 로켓, 발사대에 불과할 뿐이고
# 실제로 보내야 하는 내용은 mail을 통해 작성하고 탑재(payload)되어야 한다.

# email 라이브러리도 기본 설치이다
# 제목과 본문을 포함한 텍스트를 전달하기 위한 컨테이너
from email.mime.text import MIMEText

# Multipart란, 첨부파일을 의미한다.
from email.mime.multipart import MIMEMultipart

# 이메일 전송을 위한 함수
# 필요한 정보(매개변수)
# - 보내는 사람의 이메일: str
# - 받는 사람의 이메일: str
# - 보내는 사람의 이메일에 접근할 수 있는 비밀번호(app password): str
# - 내용/제목: str
# - 내용/본문: str
def send_email(sender_email:str, 
			receiver_email:str, 
			password:str,
			subject:str,
			body_text:str
			):
	pass

if __name__ == "__main__":
	sender = "miraclelee0613@gmail.com"
	receiver = "jslee7518@gmail.com"
	app_password = "bfzk zuql rpve kmwf"
	subject = "test1" # 제목
	body_text = "test1 내용" # 내용