import pandas as pd
from dotenv import load_dotenv
# from llama_index.experimental.query_engine import PandasQueryEngine
# from customPrompts.viz_engine_prompts import visualizer_prompt, instruction_str, response_synthesis_prompt_str
from customPrompts.agent_prompts import context, new_agent_prompt
from customTools.titanic_info_engine import titanic_info_tool
from customTools.WiKi_engine import WiKiTool
from customTools.data_answering import data_answering
from customTools.data_visualizer import data_visualizer
from llama_index.core.agent import ReActAgent
from llama_index.llms.openai import OpenAI
from utils import *
from customTools.note_engine import note_engine
import datetime

import os
load_dotenv()


tools = [data_answering, data_visualizer, titanic_info_tool, WiKiTool]

llm = OpenAI(model="gpt-3.5-turbo-instruct")
agent = ReActAgent.from_tools(tools, llm=llm, verbose=True, context=context)
# Updating the prompt
agent.update_prompts({'agent_worker:system_prompt':new_agent_prompt})

report = ""

while(prompt := input("Enter a prompt (q to quit): ")) != "q":
    result = agent.query(prompt)
    report += result.__str__()
    print(result)
    # note_engine.call(result)

images_generated = get_plots_for_report()
print(images_generated)
for image in images_generated:
    report += str(image) + '\n'

report_name = get_report_name()
note_file = os.path.join("Reports", report_name)
def save_note(note):
    if not os.path.exists(note_file):
        open(note_file, "w")
    with open(note_file, "a") as f:
        f.writelines([note + "\n"])

    return "note saved"
save_note(report)
# note_engine.call(report)

