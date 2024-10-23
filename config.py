
import os

smtp_server = 'smtp.163.com'
smtp_port = 25

sender_email = os.getenv('SENDER_EMAIL')
sender_password = os.getenv('SENDER_PASSWORD')

recipient_email = os.getenv('RECIPIENT_EMAIL')
send_subject = 'Sydney'
send_name = 'Sydney'

target_sender = os.getenv('TARGET_SENDER')

API_KEY = os.getenv('API_KEY')
BASE_URL = os.getenv('BASE_URL')

# MySQL database connection settings
mysql_host = os.getenv('MYSQL_HOST')
mysql_user = os.getenv('MYSQL_USER')
mysql_password = os.getenv('MYSQL_PASSWORD')
mysql_db = os.getenv('MYSQL_DB')

