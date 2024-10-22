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
    for email_content in email_contents:
        response = swarm_client.run(
            agent = agent_b,
            messages = [{"role":"user","content": email_content}],
        )
        print(response.messages[-1]["content"]) 
