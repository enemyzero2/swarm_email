import sys
from openai import OpenAI
import os
from swarm import Swarm, Agent
import streamlit as st
from agents import agent_b
from config import API_KEY, BASE_URL
sys.path.append('/root/swarm')

client = OpenAI(api_key=API_KEY, base_url=BASE_URL)
swarm_client = Swarm(client)

def run_agent_conversion():
    response = swarm_client.run(
        agent = agent_b,
        messages = [{"role":"user","content":"看一下现在是什么时间，然后给我发送邮件问候我。问候内容详细，温柔一点，附带对应时间的问候语，例如晚上就说晚上好，早上就说早上好，然后关心一下我的近况啥啥的。总之怎么可爱怎么来。"}],
    )

    print(response.messages[-1]["content"]) 
