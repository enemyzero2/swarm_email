import functions as ft
from swarm import Agent, Swarm
from agents import return_agents
from test import run_multi_turn_conversion,client
agents = return_agents()

run_multi_turn_conversion(openai_client=client, starting_agent=agents[1])