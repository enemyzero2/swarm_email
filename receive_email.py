import poplib
from email import parser
from datetime import datetime
from dateutil import parser as dateutil_parser
import config

def connect_to_pop3_server():
    pop3_server = 'pop.163.com'
    email_user = config.sender_email
    email_pass = config.sender_password

    server = poplib.POP3(pop3_server)
    server.user(email_user)
    server.pass_(email_pass)
    return server

def retrieve_emails(server):
    emails, _ = server.stat()
    email_list = []
    for i in range(emails):
        response, lines, _ = server.retr(i + 1)
        msg_content = b'\r\n'.join(lines).decode('utf-8')
        msg = parser.Parser().parsestr(msg_content)
        email_list.append(msg)
    return email_list

def filter_emails_by_date_and_sender(email_list, target_date, target_sender):
    filtered_emails = []
    for email in email_list:
        email_date = email['Date']
        email_sender = email['From']
        email_date = dateutil_parser.parse(email_date)  # Automatic parsing
        if email_date.date() == target_date.date() and target_sender in email_sender:
            filtered_emails.append(email)
    return filtered_emails

def extract_email_content(email):
    if email.is_multipart():
        # 多部分邮件，需要遍历每一部分
        parts = email.get_payload()
        content = ""
        for part in parts:
            if part.get_content_type() == "text/plain":  # 只提取纯文本部分
                content += part.get_payload(decode=True).decode(part.get_content_charset('utf-8'))
        return content.strip()
    else:
        # 非多部分邮件，直接解码并返回
        return email.get_payload(decode=True).decode(email.get_content_charset('utf-8')).strip()

def receive_emails():
    server = connect_to_pop3_server()
    email_list = retrieve_emails(server)
    today = datetime.now()
    target_sender = config.target_sender
    filtered_emails = filter_emails_by_date_and_sender(email_list, today, target_sender)
    email_contents = [extract_email_content(email) for email in filtered_emails]
    #print(email_contents)  # Add this line for debugging
    return email_contents
receive_emails.__doc__ = "接收来自主人的邮件"


