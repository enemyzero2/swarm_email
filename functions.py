import smtplib
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from email.header import Header
from email.utils import formataddr
from email.mime.multipart import MIMEMultipart
from config import smtp_server, smtp_port, sender_email, sender_password, recipient_email, send_subject, send_name
from models import CalendarEvent
import mysql.connector
from config import mysql_host, mysql_user, mysql_password, mysql_db

def send_email(main_text: str) -> None:
    """
    Send an email with the given main text.

    Args:
        main_text (str): The main text of the email.
    """
    try:
        # 发件人和收件人信息
        sender_name = 'sydney'
        recipient_name = 'hou'

        # 构建邮件
        message = MIMEMultipart()
        message['From'] = formataddr((str(Header(sender_name, 'utf-8')), sender_email))
        message['To'] = formataddr((str(Header(recipient_name, 'utf-8')), recipient_email))
        message['Subject'] = Header(send_subject, 'utf-8')

        # 添加邮件正文
        message.attach(MIMEText(main_text, 'plain', 'utf-8'))

        # 连接到 SMTP 服务器并发送邮件
        smtp_connection = smtplib.SMTP(smtp_server, smtp_port)
        smtp_connection.login(sender_email, sender_password)
        smtp_connection.sendmail(sender_email, recipient_email, message.as_string())
        smtp_connection.quit()

        print("Email sent successfully")
    except Exception as e:
        print("Failed to send email. Error: {}".format(e))

def connect_to_db() -> mysql.connector.connection.MySQLConnection:
    """
    Connect to the MySQL database.

    Returns:
        mysql.connector.connection.MySQLConnection: A connection to the MySQL database.
    """
    return mysql.connector.connect(
        host=mysql_host,
        user=mysql_user,
        password=mysql_password,
        database=mysql_db
    )

def add_event_to_db(event: CalendarEvent) -> None:
    """
    Add an event to the database.

    Args:
        event (CalendarEvent): The event to be added to the database.
    """
    db = connect_to_db()
    cursor = db.cursor()
    query = "INSERT INTO events (name, date, participants, more_info) VALUES (%s, %s, %s, %s)"
    values = (event.name, event.date, ','.join(event.participants), event.more_info)
    cursor.execute(query, values)
    db.commit()
    cursor.close()
    db.close()

def get_events_from_db() -> list[CalendarEvent]:
    """
    Get events from the database.

    Returns:
        list[CalendarEvent]: A list of events retrieved from the database.
    """
    db = connect_to_db()
    cursor = db.cursor()
    query = "SELECT name, date, participants, more_info FROM events"
    cursor.execute(query)
    events = []
    for (name, date, participants, more_info) in cursor:
        event = CalendarEvent(
            name=name,
            date=date,
            participants=participants.split(','),
            more_info=more_info
        )
        events.append(event)
    cursor.close()
    db.close()
    return events
