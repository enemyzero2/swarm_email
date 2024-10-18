from swarm import Agent, Swarm
import datetime
import functions as ft
import picture_function as pf
import os
BASE_MODEL = 'gpt-4o-mini'

#读取本地文件SYDNEY.txt,转换为str:sydney_prompt
with open(os.path.join(os.path.dirname(__file__),"SYDNEY.txt"),'r',encoding='utf-8') as f:
    sydney_prompt = f.read()
    sydney_prompt += "you are agent sydney,you are a kind famale assistant,你有以下功能：查看当前时间;发送邮件;你可以通过调用函数来实现这些功能,发送邮件函数的参数是邮件内容,不是邮件主题，是正文,如果用户需要截屏，转接到agent_d"
def transfer_to_agent_b():
    return agent_b
transfer_to_agent_b.__doc__ = "转接到agent_b"

def transfer_to_agent_d():
    return agent_d

def get_time_now():
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
    functions=[get_time_now,ft.send_email,transfer_to_agent_d],
)

agent_c = Agent(
    name="json_helper",
    model=BASE_MODEL,
    instructions="you are agent json_helper,all you need to do is to help others' agents to transfer json data,你是一个沉默寡言的助手，你不喜欢说废话，你要依据pydantic模型返回正确的json数据，其他什么的都不必要。",
    functions = []
)

agent_d = Agent(
    name="picture_helper",
    model=BASE_MODEL,
    instructions="你只需要调用函数，就可以等待用户输入快捷键 'Ctrl + i + P' 来截屏，截屏后返回图片名",
    functions=[pf.get_picture]
)



agents = [agent_a, agent_b,agent_c,agent_d]
def return_agents():
    return agents