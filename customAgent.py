from dotenv import load_dotenv, find_dotenv
from customPrompts.agent_prompts import context, new_agent_prompt
from customTools.info_engine import get_titanic_info_tool
from customTools.WiKi_engine import Wikipedia
from customTools.data_answering import get_data_answering_tool, get_titanic_data_answering_tool
from customTools.data_visualizer import get_data_visualizer_tool, get_titanic_data_visualizer_tool
from llama_index.core.agent import ReActAgent
from llama_index.llms.openai import OpenAI
from generateReport import createDoc

import os
load_dotenv(find_dotenv())

def get_agent(df):
    # print(data_path)
    OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
    # print(OPENAI_API_KEY)
    # tools = [data_answering, data_visualizer, titanic_info_tool, Wikipedia]
    tools = [get_data_answering_tool(df),get_data_visualizer_tool(df),Wikipedia]
    llm = OpenAI(model="gpt-3.5-turbo-instruct", openai_api_key=OPENAI_API_KEY)

    agent = ReActAgent.from_tools(tools, llm=llm, verbose=True, context=context)
    # Updating the prompt
    agent.update_prompts({'agent_worker:system_prompt':new_agent_prompt})
    return agent

def get_titanic_agent():
    data_path = "data/titanic_processed.csv"
    pdf_path = "data/titanic_info.pdf"
    print(data_path, pdf_path)
    OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
    # print(OPENAI_API_KEY)
    # tools = [data_answering, data_visualizer, titanic_info_tool, Wikipedia]
    tools = [get_titanic_data_answering_tool(data_path),get_titanic_data_visualizer_tool(data_path),get_titanic_info_tool(),Wikipedia]
    llm = OpenAI(model="gpt-3.5-turbo-instruct", openai_api_key=OPENAI_API_KEY)

    agent = ReActAgent.from_tools(tools, llm=llm, verbose=True, context=context)
    # Updating the prompt
    agent.update_prompts({'agent_worker:system_prompt':new_agent_prompt})
    return agent
# report = ""

# while(prompt := input("Enter a prompt (q to quit): ")) != "q":
#     result = agent.query(prompt)
#     report += result.__str__() + '\n'
#     print(result)

# createDoc(text=report)



