import poplib
from email import parser
from datetime import datetime
from dateutil import parser as dateutil_parser
import config

def connect_to_pop3_server() -> poplib.POP3:
    """
    Connect to the POP3 server.

    Returns:
        poplib.POP3: The connected POP3 server instance.
    """
    pop3_server = 'pop.163.com'
    email_user = config.sender_email
    email_pass = config.sender_password

    server = poplib.POP3(pop3_server)
    server.user(email_user)
    server.pass_(email_pass)
    return server

def retrieve_emails(server: poplib.POP3) -> list:
    """
    Retrieve emails from the POP3 server.

    Args:
        server (poplib.POP3): The connected POP3 server instance.

    Returns:
        list: A list of email messages.
    """
    emails, _ = server.stat()
    email_list = []
    for i in range(emails):
        response, lines, _ = server.retr(i + 1)
        msg_content = b'\r\n'.join(lines).decode('utf-8')
        msg = parser.Parser().parsestr(msg_content)
        email_list.append(msg)
    return email_list

def filter_emails_by_date_and_sender(email_list: list, target_date: datetime, target_sender: str) -> list:
    """
    Filter emails by date and sender.

    Args:
        email_list (list): A list of email messages.
        target_date (datetime): The target date to filter emails.
        target_sender (str): The target sender email address.

    Returns:
        list: A list of filtered email messages.
    """
    filtered_emails = []
    for email in email_list:
        email_date = email['Date']
        email_sender = email['From']
        email_date = dateutil_parser.parse(email_date)  # Automatic parsing
        if email_date.date() == target_date.date() and target_sender in email_sender:
            filtered_emails.append(email)
    return filtered_emails

def extract_email_content(email: parser.Parser) -> str:
    """
    Extract the content of an email.

    Args:
        email (parser.Parser): The email message.

    Returns:
        str: The extracted email content.
    """
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

def receive_emails() -> list:
    """
    Receives emails from the POP3 server and filters them based on the current date and target sender.

    This function connects to a POP3 server, retrieves all available emails, and filters the list of emails by 
    checking if the sender matches the specified target sender and if the email was sent on the current date.
    It returns a list of the contents of the filtered emails.

    Args:
        None

    Returns:
        list: A list of strings, where each string is the content of an email that matches the criteria.
        
    Raises:
        ConnectionError: If the connection to the POP3 server fails.
        ValueError: If the filtering criteria are not properly defined.

    Example:
        >>> emails = receive_emails()
        >>> print(emails)
        ['Email 1 content', 'Email 2 content']
    """
    server = connect_to_pop3_server()
    email_list = retrieve_emails(server)
    today = datetime.now()
    target_sender = config.target_sender
    filtered_emails = filter_emails_by_date_and_sender(email_list, today, target_sender)
    email_contents = [extract_email_content(email) for email in filtered_emails]
    return email_contents

receive_emails.__doc__ = "接收来自主人的邮件"
