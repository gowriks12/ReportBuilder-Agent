import pandas as pd
import os
from dotenv import load_dotenv
from llama_index.experimental.query_engine import PandasQueryEngine
from llama_index.experimental.query_engine.pandas import (
    PandasInstructionParser,
)
from engine_prompts import pandas_prompt, instruction_str, context
from agent_prompts import *
load_dotenv()
from note_engine import note_engine
from llama_index.core.tools import QueryEngineTool, ToolMetadata
from llama_index.core.agent import ReActAgent
from llama_index.llms.openai import OpenAI

df = pd.read_csv("data/titanic.csv")
# print(df.head())

df_query_engine = PandasQueryEngine(df = df, verbose=True, instruction_str=instruction_str) #specifying the query engine for RAG
df_query_engine.update_prompts({"pandas_prompt": pandas_prompt})
# df_query_engine.query("What is the ratio of male/female in this dataset?")
# pandas_output_parser = PandasInstructionParser(df)

tools = [note_engine, QueryEngineTool(query_engine=df_query_engine, metadata=ToolMetadata(
    name="titanic_data",
    description="This gives information about the passengers in titanic when it was hit and if they survived or no"
        ),
    ),
]

llm = OpenAI(model="gpt-3.5-turbo-instruct")
agent = ReActAgent.from_tools(tools, llm=llm, verbose=True, context=context)
# Updating the prompt
agent.update_prompts({'agent_worker:system_prompt':new_agent_prompt})

while(prompt := input("Enter a prompt (q to quit): ")) != "q":
    result = agent.query(prompt)
    print(result)
    # note_engine.call(result)


