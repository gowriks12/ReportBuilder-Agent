from llama_index.core.tools.ondemand_loader_tool import OnDemandLoaderTool
from llama_index.readers.wikipedia import WikipediaReader

reader = WikipediaReader()

Wikipedia = OnDemandLoaderTool.from_defaults(
    reader,
    name="Wikipedia",
    description="A tool for loading and querying articles from Wikipedia, input format is as follows:"
                "{pages:['query_keyword'],query_str:'What's the arts and culture scene in Berlin?'}",
)