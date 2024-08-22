from llama_index.core.tools.ondemand_loader_tool import OnDemandLoaderTool
from llama_index.readers.wikipedia import WikipediaReader
# from llama_index.tools.wikipedia import WikipediaToolSpec
# from llama_index.tools.tool_spec.load_and_search.base import LoadAndSearchToolSpec
from typing import List

from pydantic import BaseModel

# wiki_spec = WikipediaToolSpec()
# # Get the search wikipedia tool
# tool = wiki_spec.to_tool_list()[1]
# Wikipedia = LoadAndSearchToolSpec.from_defaults(tool).to_tool_list()
reader = WikipediaReader()

Wikipedia = OnDemandLoaderTool.from_defaults(
    reader,
    name="Wikipedia",
    description="A tool for loading and querying articles from Wikipedia, input format is as follows:"
                "{pages:['query_keyword'],query_str:'What's the arts and culture scene in Berlin?'}",
)