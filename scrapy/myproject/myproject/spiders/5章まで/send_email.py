import smtplib
from email.mime.text import MIMEText
from email.header import Header

msg = MIMEText('メールの本文です。')
msg['Subject'] = Header('メールの本文です。')
msg['From'] = 'koudabusiness@example.com'
msg['To'] = 'koudabusiness@example.com'

with smtplib.SMTP('smtp.gmail.com') as smtp:
	smtp.login('koudabusiness','dmjdmj123')
	smtp.send_message(msg)