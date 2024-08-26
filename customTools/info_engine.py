import os
from llama_index.core import StorageContext, VectorStoreIndex, load_index_from_storage
from llama_index.readers.file import PDFReader
from llama_index.core.tools import QueryEngineTool, ToolMetadata
from llama_index.core import StorageContext, load_index_from_storage


# def create_index_path(pdf_path):
#     index = None
#     if pdf_path == "data/titanic_info.pdf":
#         index_path = "data/titanic_info_index"
#         # print("loading index", index_path)
#         return index_path
#     else:
#         index_path = "data/titanic_info_index"
#         pdf = PDFReader().load_data(file=pdf_path)
#         index = VectorStoreIndex.from_documents(pdf, show_progress=True)
#         index.storage_context.persist(persist_dir=index_path)
#         return index_path


def get_titanic_info_tool():
    index_path = "data/titanic_info_index"
    if os.path.exists(index_path):
        titanic_index = load_index_from_storage(
            StorageContext.from_defaults(persist_dir=index_path)
        )
    else:
        pdf = PDFReader().load_data(file="data/titanic_info.pdf")
        titanic_index = VectorStoreIndex.from_documents(pdf, show_progress=True)
        titanic_index.storage_context.persist(persist_dir=index_path)

    titanic_info_engine = titanic_index.as_query_engine()
    titanic_info_tool = QueryEngineTool(
        query_engine=titanic_info_engine,
        metadata=ToolMetadata(
            name="titanic_info_data",
            description="This gives detailed information about Titanic Ship",
        ),
    )
    return titanic_info_tool


# def get_info_tool(pdf_path):
#     index_path = create_index_path(pdf_path)
#     index = load_index_from_storage(
#         StorageContext.from_defaults(persist_dir=index_path)
#     )
#
#     info_engine = index.as_query_engine()
#     info_tool = QueryEngineTool(
#             query_engine=info_engine,
#             metadata=ToolMetadata(
#                 name="info_data",
#                 description="This gives information about certain topic, use it to answer factual questions about the topic",
#         ),
#     )
#     return info_tool
# print(titanic_info_engine.query("When did titanic sink?"))
