from llama_index.core.tools.ondemand_loader_tool import OnDemandLoaderTool
from llama_index.readers.wikipedia import WikipediaReader
from typing import List

from pydantic import BaseModel

reader = WikipediaReader()

WiKiTool = OnDemandLoaderTool.from_defaults(
    reader,
    name="Wikipedia Tool",
    description="A tool for loading and querying articles from Wikipedia",
)