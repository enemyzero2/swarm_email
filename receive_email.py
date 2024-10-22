import poplib
from email import parser
from datetime import datetime
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
        email_date = datetime.strptime(email_date, '%a, %d %b %Y %H:%M:%S %z')
        if email_date.date() == target_date.date() and target_sender in email_sender:
            filtered_emails.append(email)
    return filtered_emails

def extract_email_content(email):
    return email.get_payload()

def receive_emails():
    server = connect_to_pop3_server()
    email_list = retrieve_emails(server)
    today = datetime.now()
    target_sender = 'specified_sender@example.com'
    filtered_emails = filter_emails_by_date_and_sender(email_list, today, target_sender)
    email_contents = [extract_email_content(email) for email in filtered_emails]
    return email_contents
