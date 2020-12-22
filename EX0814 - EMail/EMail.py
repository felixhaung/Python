import smtplib
from email.mime.text import MIMEText
 
user = 'aes.admin@amkor.com'

re = 'felix.huang@amkor.com'
msg=MIMEText('Python test...', 'plain', 'utf-8')
msg['Subject'] = 'Test'
msg['From'] = user
msg['To'] = re

try:
    server = smtplib.SMTP('exim.tw.ds.amkor.com')
    server.sendmail(user, re, msg.as_string())
    print("sucess")
except smtplib.SMTPException:
    print("fail")
