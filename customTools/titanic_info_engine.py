import os
from llama_index.core import StorageContext, VectorStoreIndex, load_index_from_storage
from llama_index.readers.file import PDFReader
from llama_index.core.tools import QueryEngineTool, ToolMetadata
from llama_index.core import StorageContext, load_index_from_storage


# def get_index(data, index_name):
#     index = None
#     if not os.path.exists(index_name):
#         print("building index", index_name)
#         index = VectorStoreIndex.from_documents(data, show_progress=True)
#         index.storage_context.persist(persist_dir=index_name)
#     else:
#         index = load_index_from_storage(
#             StorageContext.from_defaults(persist_dir=index_name)
#         )
#     return index


def get_index(index_path):
    index = None
    if os.path.exists(index_path):
        index = load_index_from_storage(
            StorageContext.from_defaults(persist_dir=index_path)
        )
        print("loading index", index_path)
    else:
        pdf_path = "data/titanic_info.pdf"
        titanic_pdf = PDFReader().load_data(file=pdf_path)
        index = VectorStoreIndex.from_documents(titanic_pdf, show_progress=True)
        index.storage_context.persist(persist_dir=index_path)

    return index


index_path = "data/titanic_info_index"
titanic_index = get_index(index_path)


titanic_info_engine = titanic_index.as_query_engine()
titanic_info_tool = QueryEngineTool(
        query_engine=titanic_info_engine,
        metadata=ToolMetadata(
            name="titanic_info_data",
            description="This gives detailed information about Titanic Ship",
    ),
)
# print(titanic_info_engine.query("When did titanic sink?"))
