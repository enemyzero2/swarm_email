import sys
from openai import OpenAI
import os
from swarm import Swarm, Agent
import streamlit as st
from agents import agent_b
from config import API_KEY, BASE_URL
from receive_email import receive_emails
sys.path.append('/root/swarm')

client = OpenAI(api_key=API_KEY, base_url=BASE_URL)
swarm_client = Swarm(client)

def run_agent_conversion():
    email_contents = receive_emails()
    
    # 合并所有邮件内容为单个字符串
    combined_content = "\n\n".join(
        [f"第 {i+1} 封邮件内容:\n{content}" for i, content in enumerate(email_contents)]
    )
    #print(combined_content)
    # 只调用一次 swarm_client.run()
    response = swarm_client.run(
        agent=agent_b,
        messages=[{"role": "user", "content": f"对方发送的邮件内容:\n{combined_content}"}],
        debug=True
    )

    # 打印最后的响应内容
    print(response.messages[-1]["content"])
