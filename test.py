import sys
from openai import OpenAI
import os
from swarm import Swarm, Agent
import streamlit as st
from agents import agent_b
sys.path.append('/root/swarm')

API_KEY = 'sk-BPv3we5kZVzAGA4SJ3mBYZQuzNAHB47iLTr78s7OA4VE1ujW'
BASE_URL = 'https://xdaicn.top/v1'

#API_KEY = 'sk-leijDw1a3T6boFYyP3aJYGgWtb7haYhfsvMwSLVeAcKruADJ'
#BASE_URL = 'https://api.deepbricks.ai/v1/'
client = OpenAI(api_key=API_KEY, base_url=BASE_URL)
swarm_client = Swarm(client)

def run_agent_conversion():
    response = swarm_client.run(
        agent = agent_b,
        messages = [{"role":"user","content":"看一下现在是什么时间，然后给我发送邮件问候我。（早上好？中午好？晚上好？）问候内容30字左右"}],
    )

    print(response.messages[-1]["content"]) 