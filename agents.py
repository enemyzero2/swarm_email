import json
from swarm import Agent, Swarm
import datetime
import functions as ft
import os
from receive_email import receive_emails
from models import CalendarEvent
from database import add_event_to_db, get_events_from_db

BASE_MODEL = 'gpt-4o-2024-08-06'

# 读取本地文件SYDNEY.txt,转换为str:sydney_prompt
with open(os.path.join(os.path.dirname(__file__), "SYDNEY.txt"), 'r', encoding='utf-8') as f:
    sydney_prompt = f.read()
    sydney_prompt += "you are agent sydney,you are a kind famale assistant,你有以下功能：查看当前时间;发送邮件;你可以通过调用函数来实现这些功能,发送邮件函数的参数是邮件内容,不是邮件主题，是正文"


def transfer_to_agent_b() -> Agent:
    """转接到agent_b"""
    return agent_b

def transfer_to_agent_e() -> Agent:
    """转接到agent_e"""
    return agent_e
transfer_to_agent_e.__doc__ = "每当需要进行数据库操作时，你可以转接到ela，ela会帮助你完成数据库操作。"


def get_time_now() -> datetime.datetime:
    """获取当前时间"""
    return datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=8)))


agent_a = Agent(
    name='agent_a',
    instructions="you are agent albert,you are able to transfer to agent sydney by using functions",
    model=BASE_MODEL,
    functions=[transfer_to_agent_b],
)

agent_b = Agent(
    name="sydney",
    model=BASE_MODEL,
    instructions=sydney_prompt,
    functions=[get_time_now, ft.send_email, receive_emails,transfer_to_agent_e],
)

agent_c = Agent(
    name="json_helper",
    model=BASE_MODEL,
    instructions="you are agent json_helper,all you need to do is to help others' agents to transfer json data,你是一个沉默寡言的助手，你不喜欢说废话，你要依据pydantic模型返回正确的json数据，其他什么的都不必要。",
    functions=[]
)


def add_event(event: str) -> None:
    """
    Add a calendar event to the database.

    This function takes a JSON string representing an event, converts it to a dictionary, and then 
    creates a `CalendarEvent` object. The event includes information such as the event name, date, 
    participants, and additional details. It then calls a helper function to insert the event into 
    the database.

    Args:
        event (str): A JSON string containing details of the event. The expected structure includes:
                     - name (str): The name of the event.
                     - date (str): The event's date (in YYYY-MM-DD format usually).
                     - participants (list of str): A list of participants involved in the event.
                     - more_info (str): Additional information about the event.

    Returns:
        None

    Example:
        >>> event_json = '{"name": "Meeting", "date": "2024-10-30", "participants": ["Alice", "Bob"], "more_info": "Project discussion"}'
        >>> add_event(event_json)
    """
    # Convert the event string (JSON format) to a dictionary
    event_data = json.loads(event)

    # Create a CalendarEvent object from the dictionary
    event_obj = CalendarEvent(**event_data)

    # Call the helper function to add the event to the database
    add_event_to_db(event_obj)


def get_events() -> list[CalendarEvent]:
    """从数据库获取事件"""
    return get_events_from_db()


agent_e = Agent(
    name="ela",
    model=BASE_MODEL,
    instructions="you are agent ela, you are responsible for managing the database. You will track email content and add necessary events and schedules to the database.the base model is: class CalendarEvent(BaseModel):/n name: str/n date: str/n participants: List[str]/n more_info: str,/n",
    functions=[add_event, get_events],
)

agents = [agent_a, agent_b, agent_c, agent_e]


def return_agents() -> list[Agent]:
    """返回所有代理"""
    return agents
