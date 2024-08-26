import pandas as pd
from dotenv import load_dotenv
from llama_index.experimental.query_engine import PandasQueryEngine
from customPrompts.data_engine_prompts import pandas_qna_prompt, instruction_str, response_synthesis_prompt_str
from llama_index.core.tools import QueryEngineTool, ToolMetadata

load_dotenv()
def get_data_answering_tool(df):
    # df = pd.read_csv(data_path)

    df_query_engine = PandasQueryEngine(df = df, verbose=True, instruction_str=instruction_str) #specifying the query engine for RAG
    df_query_engine.update_prompts({"pandas_prompt": pandas_qna_prompt, "response_synthesis_prompt":response_synthesis_prompt_str})

    # df_query_engine.query("How many passengers survived in titanic?")
    # df_query_engine.query("What is the correlation factor between age and survival rate, explain?")
    # df_query_engine.query("What is the Male to female ratio amongst the survivors?")

    data_answering = QueryEngineTool(query_engine=df_query_engine, metadata=ToolMetadata(
        name="data_answering",
        description="This tool helps in answering data analytic and statistical questions about provided data",
        ),
    )
    return data_answering

def get_titanic_data_answering_tool(data_path="data/titanic_processed.csv"):
    df = pd.read_csv(data_path)

    df_query_engine = PandasQueryEngine(df = df, verbose=True, instruction_str=instruction_str) #specifying the query engine for RAG
    df_query_engine.update_prompts({"pandas_prompt": pandas_qna_prompt, "response_synthesis_prompt":response_synthesis_prompt_str})

    # df_query_engine.query("How many passengers survived in titanic?")
    # df_query_engine.query("What is the correlation factor between age and survival rate, explain?")
    # df_query_engine.query("What is the Male to female ratio amongst the survivors?")

    data_answering = QueryEngineTool(query_engine=df_query_engine, metadata=ToolMetadata(
        name="data_answering",
        description="This tool helps in answering data analytic and statistical questions about titanic passenger data",
        ),
    )
    return data_answering
