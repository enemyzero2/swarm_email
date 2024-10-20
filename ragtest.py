from lightrag import LightRAG,QueryParam
from lightrag.llm import gpt_4o_mini_complete, gpt_4o_complete
import os
WORKING_DIR = "./MEMORYs"

if not os.path.exists(WORKING_DIR):
    os.makedirs(WORKING_DIR)

rag = LightRAG(
    working_dir = WORKING_DIR,
    llm_model_func = gpt_4o_mini_complete
)

with open("./MEMORYs/memory.txt","r",encoding = "utf-8") as f:
    rag.insert(f.read())

print(rag.query("who is luka?and who is his wife?",param = QueryParam(mode ="naive")))