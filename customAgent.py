from dotenv import load_dotenv, find_dotenv
from customPrompts.agent_prompts import context, new_agent_prompt
from customTools.titanic_info_engine import titanic_info_tool
from customTools.WiKi_engine import Wikipedia
from customTools.data_answering import data_answering
from customTools.data_visualizer import data_visualizer
from llama_index.core.agent import ReActAgent
from llama_index.llms.openai import OpenAI
from generateReport import createDoc

import os
load_dotenv(find_dotenv())

OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
# print(OPENAI_API_KEY)
tools = [data_answering, data_visualizer, titanic_info_tool, Wikipedia]

llm = OpenAI(model="gpt-3.5-turbo-instruct", openai_api_key=OPENAI_API_KEY)

agent = ReActAgent.from_tools(tools, llm=llm, verbose=True, context=context)
# Updating the prompt
agent.update_prompts({'agent_worker:system_prompt':new_agent_prompt})


# report = ""

# while(prompt := input("Enter a prompt (q to quit): ")) != "q":
#     result = agent.query(prompt)
#     report += result.__str__() + '\n'
#     print(result)

# createDoc(text=report)



