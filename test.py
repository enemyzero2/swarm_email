import sys
import os
import streamlit as st
from openai import OpenAI
from swarm import Swarm, Agent
from agents import agent_b
from config import API_KEY, BASE_URL
from receive_email import receive_emails

sys.path.append('/root/swarm')

client = OpenAI(api_key=API_KEY, base_url=BASE_URL)
swarm_client = Swarm(client)

def run_agent_conversion() -> None:
    """
    Run the agent conversion process.

    This function receives emails, combines their content, and runs the agent conversion process
    using the Swarm client. The final response content is printed.
    """
    email_contents = receive_emails()
    
    # 合并所有邮件内容为单个字符串
    combined_content = "\n\n".join(
        [f"第 {i+1} 封邮件内容:\n{content}" for i, content in enumerate(email_contents)]
    )
    #print(combined_content)
    # 只调用一次 swarm_client.run()
    response = swarm_client.run(
        agent=agent_b,
       messages=[{"role": "user", "content": f"对方发送的邮件内容:\n{combined_content}"},
                  {"role": "user","content":"看一下现在是什么时间，然后给我发送邮件问候我。问候内容详细，温柔一点，附带对应时间的问候语，例如晚上就说晚上好，早上就说早上好，如果我今天有发邮件，记得回信"},],
        #messages = [{"role": "user","content":"看一下现在是什么时间，然后给我发送邮件问候我。问候内容详细，温柔一点，附带对应时间的问候语，例如晚上就说晚上好，早上就说早上好，然后关心一下我的近况啥啥的。总之怎么可爱怎么来。"}],
        #debug=True
    )

    # 打印最后的响应内容
    print(response.messages[-1]["content"])
