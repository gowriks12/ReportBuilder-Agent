import pandas as pd
from dotenv import load_dotenv
from llama_index.experimental.query_engine import PandasQueryEngine
from customPrompts.viz_engine_prompts import visualizer_prompt, instruction_str, response_synthesis_prompt_str

from llama_index.core.tools import QueryEngineTool, ToolMetadata

load_dotenv()


df = pd.read_csv("data/titanic_processed.csv")
# print(df.head())

df_query_engine = PandasQueryEngine(df = df, verbose=True, instruction_str=instruction_str) #specifying the query engine for RAG
df_query_engine.update_prompts({"pandas_prompt": visualizer_prompt, "response_synthesis_prompt":response_synthesis_prompt_str})
# print(df_query_engine._get_prompts())
# df_query_engine.query("plot a histogram of age in titanic")
# df_query_engine.query("Create a bar plot representing ratio of male and female that survived titanic disaster")
# df_query_engine.query("plot a bar graph depicting correlation between survived and age, divide the age groups into buckets of 10 years and explain the plot")

data_visualizer = QueryEngineTool(query_engine=df_query_engine, metadata=ToolMetadata(
    name="titanic_data_visualizer",
    description="This tool helps in titanic passenger data visualization by creating plots on titanic passenger data",
    ),
)
