import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.utils import formataddr

smtp_server = 'smtp.163.com'
smtp_port = 25

sender_email = '15239288661@163.com'
sender_password = 'VHeaV389jFjd3cMe'

recipient_email = '2939827325@qq.com'
send_subject = 'Sydney'
send_name = 'Sydney'
def send_email(main_text:str):
    try:
        # 发件人和收件人信息
        sender_name = 'sydney'
        recipient_name = 'hou'

        # 构建邮件
        message = MIMEText(main_text, 'plain', 'utf-8')
        message['From'] = formataddr((str(Header(sender_name, 'utf-8')), sender_email))
        message['To'] = formataddr((str(Header(recipient_name, 'utf-8')), recipient_email))
        message['Subject'] = Header(send_subject, 'utf-8')

        # 连接到 SMTP 服务器并发送邮件
        smtp_connection = smtplib.SMTP(smtp_server, smtp_port)
        smtp_connection.login(sender_email, sender_password)
        smtp_connection.sendmail(sender_email, recipient_email, message.as_string())
        smtp_connection.quit()

        print("Email sent successfully")
    except Exception as e:
        print("Failed to send email. Error: {}".format(e))