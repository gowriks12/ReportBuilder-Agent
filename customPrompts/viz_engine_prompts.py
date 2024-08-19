from llama_index.core import PromptTemplate


qna_instruction_str = """\
    1. Convert the query to executable Python code using Pandas.
    2. The final line of code should be a Python expression that can be called with the `eval()` function.
    3. The code should represent a solution to the query.
    4. PRINT ONLY THE EXPRESSION.
    5. Do not quote the expression."""

instruction_str = """\
    1. Convert the query to executable Python code using Pandas and matplotlib.pyplot.
    2. STRICTLY RETURN ONLY CODE WITHOUT IMPORT STATEMENTS
    3. Set ax = pandas expression and add any necessary pyplot styling attributes to this variable.
    4. Save the plot in current directory using plt.savefig(), give image a valid name as per query.
    4. The final line of code should be plt.show() Python expression that can be called with the `eval()` function to display a plot.
    5. The Plot should represent a solution to the query.
    """

visualizer_prompt = PromptTemplate(
    """\
    You are working with a pandas dataframe in Python.
    The name of the dataframe is `df`.
    This is the result of `print(df.head())`:
    {df_str}

    Follow these instructions:
    {instruction_str}
    Query: {query_str}

    Expression: """
)

pandas_qna_prompt = PromptTemplate(
    """\
    You are working with a pandas dataframe in Python.
    The name of the dataframe is `df`.
    This is the result of `print(df.head())`:
    {df_str}

    Follow these instructions:
    {qna_instruction_str}
    Query: {query_str}

    Expression: """
)

response_synthesis_prompt_str = (
    "Given an input question, synthesize a response or return image of plot from the query results.\n"
    "Query: {query_str}\n\n"
    "Pandas Instructions (optional):\n{pandas_instructions}\n\n"
    "Pandas Output: {pandas_output}\n\n"
    "Response: "
)

