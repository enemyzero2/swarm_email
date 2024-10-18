import sys
from openai import OpenAI
import os
from swarm import Swarm, Agent
import streamlit as st

sys.path.append('/root/swarm')

API_KEY = 'sk-BPv3we5kZVzAGA4SJ3mBYZQuzNAHB47iLTr78s7OA4VE1ujW'
BASE_URL = 'https://xdaicn.top/v1'

#API_KEY = 'sk-leijDw1a3T6boFYyP3aJYGgWtb7haYhfsvMwSLVeAcKruADJ'
#BASE_URL = 'https://api.deepbricks.ai/v1/'
client = OpenAI(api_key=API_KEY, base_url=BASE_URL)
swarm_client = Swarm(client)

def process_and_print_streaming_response(response):
    content = ""
    last_sender = ""

    # 处理响应中的每一个片段
    for chunk in response:
        if "sender" in chunk:
            last_sender = chunk["sender"]  # 保存消息发送者的名字

        if "content" in chunk and chunk["content"] is not None:
            # 如果当前内容为空并且有消息发送者，输出发送者名字
            if not content and last_sender:
                st.write(f"\033[94m{last_sender}:\033[0m")
                last_sender = ""
            # 输出消息内容
            st.write(chunk["content"], end="", flush=True)
            content += chunk["content"]

        if "tool_calls" in chunk and chunk["tool_calls"] is not None:
            # 处理工具调用
            for tool_call in chunk["tool_calls"]:
                f = tool_call["function"]
                name = f["name"]
                if not name:
                    continue
                # 输出工具调用的函数名
                st.write(f"\033[94m{last_sender}: \033[95m{name}\033[0m()")

        if "delim" in chunk and chunk["delim"] == "end" and content:
            # 处理消息结束的情况，换行表示结束
            st.write()  # End of response message
            content = ""

        if "response" in chunk:
            # 返回最终的完整响应
            return chunk["response"]



def run_multi_turn_conversion(
        openai_client,
        starting_agent,
        context_variables=None,
        debug=False,
) -> None:
    client = Swarm(openai_client)

    st.markdown('## 开启Swarm对话 🐝')

    # 初始化对话
    messages = []
    agent = starting_agent

    user_input = ""
    while user_input.lower() not in ["exit", "quit"]:
        user_input = st.text_input("User:", key="user_input")
        if user_input.lower() in ["exit", "quit"]:
            st.markdown('## 对话结束 🛑')
            break

        messages.append({"role": "user", "content": user_input})

        response = client.run(
            agent=agent,
            messages=messages,
            context_variables=context_variables or {},
            debug=debug,
        )

        for message in response.messages:
            if message["role"] == "user":
                st.markdown(f"**User**: {message['content']}")
            elif message["role"] == "assistant":
                st.markdown(f"**{agent.name}**: {message['content']}")

        messages.extend(response.messages)
        agent = response.agent

    st.stop()


