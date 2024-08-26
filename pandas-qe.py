import pandas as pd
from dotenv import load_dotenv
from llama_index.experimental.query_engine import PandasQueryEngine
from customPrompts.viz_engine_prompts import visualizer_prompt, instruction_str, response_synthesis_prompt_str

load_dotenv()

df = pd.read_csv("data/titanic.csv")
# print(df.head())

df_query_engine = PandasQueryEngine(df = df, verbose=True, instruction_str=instruction_str) #specifying the query engine for RAG
df_query_engine.update_prompts({"pandas_prompt": visualizer_prompt, "response_synthesis_prompt":response_synthesis_prompt_str})
# print(df_query_engine._get_prompts())
# df_query_engine.query("plot a histogram of age in titanic")
df_query_engine.query("Create a bar plot representing ratio of male and female that survived titanic disaster")
# respo = df_query_engine.query("plot a histogram of age in titanic")
# plt_r = respo
# plt_r.show()
# print(respo)
# pandas_output_parser = PandasInstructionParser(df)

# tools = [note_engine, QueryEngineTool(query_engine=df_query_engine, metadata=ToolMetadata(
#     name="titanic_data",
#     description="This gives information about the passengers in titanic when it was hit and if they survived or no"
#         ),
#     ),
# ]
#
# llm = OpenAI(model="gpt-3.5-turbo-instruct")
# agent = ReActAgent.from_tools(tools, llm=llm, verbose=True, context=context)
# # Updating the prompt
# agent.update_prompts({'agent_worker:system_prompt':new_agent_prompt})
#
# while(prompt := input("Enter a prompt (q to quit): ")) != "q":
#     result = agent.query(prompt)
#     print(result)
#     # note_engine.call(result)
#

