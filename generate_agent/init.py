from typing import List, Optional
from openai import OpenAI
import json
from swarm_email.swarm import Swarm, Agent  # 修改这行
from config import API_KEY, BASE_URL

def create_new_agent(
    name: str,
    instructions: str,
    model: str = "gpt-4o-mini",
    functions: List = None
) -> str:
    """Create a new agent with specified parameters"""
    agent = Agent(
        name=name,
        instructions=instructions,
        model=model,
        functions=functions or []
    )
    return json.dumps({"status": "success", "agent": agent.name})

def create_function(
    name: str,
    description: str,
    parameters: dict
) -> str:
    """Create a new function definition that can be used by agents"""
    function_template = f"""
def {name}({', '.join(parameters.keys())}):
    \"\"\"{description}\"\"\"
    # Function implementation will be added later
    pass
    """
    return json.dumps({
        "status": "success",
        "function": name,
        "definition": function_template
    })

def basic_operation(operation: str, data: str) -> str:
    """Perform basic operations like data processing, calculation etc."""
    return json.dumps({
        "status": "success",
        "result": f"Performed {operation} on {data}"
    })

# 创建一个主管理者Agent
manager_agent = Agent(
    name="AgentManager",
    model="gpt-4o-mini",
    instructions="""You are an agent manager responsible for creating and coordinating other agents.
    When a task requires specific expertise, you can create new specialized agents.
    You can also create new functions when needed.
    Always analyze the task first and decide if you need to create new agents or functions.""",
    functions=[create_new_agent, create_function, basic_operation]
)

# 创建一个Agent构建专家
agent_builder = Agent(
    name="AgentBuilder",
    model="gpt-4o-mini",
    instructions="""You are an expert in designing and creating new agents.
    Your role is to create specialized agents with appropriate instructions and functions.
    Consider the specific requirements and context when designing new agents.""",
    functions=[create_new_agent, create_function]
)

# 使用示例
if __name__ == "__main__":
    client = OpenAI(api_key=API_KEY, base_url=BASE_URL)
    swarm = Swarm(client)
    
    # 示例对话
    messages = [{
        "role": "user",
        "content": "I need an agent that can help me with data analysis"
    }]
    
    response = swarm.run(
        agent=manager_agent,
        messages=messages,
        debug=True
    ) 