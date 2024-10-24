import mysql.connector
from models import CalendarEvent
from config import mysql_host, mysql_user, mysql_password, mysql_db

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
