import os

smtp_server = 'smtp.163.com'
"""SMTP server address"""

smtp_port = 25
"""SMTP server port"""

sender_email = os.getenv('SENDER_EMAIL')
"""Sender email address"""

sender_password = os.getenv('SENDER_PASSWORD')
"""Sender email password"""

recipient_email = os.getenv('RECIPIENT_EMAIL')
"""Recipient email address"""

send_subject = 'Sydney'
"""Email subject"""

send_name = 'Sydney'
"""Sender name"""

target_sender = os.getenv('TARGET_SENDER')
"""Target sender email address"""

API_KEY = os.getenv('API_KEY')
"""API key"""

BASE_URL = os.getenv('BASE_URL')
"""Base URL"""

# MySQL database connection settings
mysql_host = os.getenv('MYSQL_HOST')
"""MySQL host"""

mysql_user = os.getenv('MYSQL_USER')
"""MySQL user"""

mysql_password = os.getenv('MYSQL_PASSWORD')
"""MySQL password"""

mysql_db = os.getenv('MYSQL_DB')
"""MySQL database name"""
