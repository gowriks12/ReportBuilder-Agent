import os
from llama_index.core import StorageContext, VectorStoreIndex, load_index_from_storage
from llama_index.core import SimpleDirectoryReader
from llama_index.readers.file import PDFReader


def get_index(data, index_name):
    index = None
    if not os.path.exists(index_name):
        print("building index", index_name)
        index = VectorStoreIndex.from_documents(data, show_progress=True)
        index.storage_context.persist(persist_dir=index_name)
    else:
        index = load_index_from_storage(
            StorageContext.from_defaults(persist_dir=index_name)
        )
    return index


# pdf_path = os.path.join("data", "Canada.pdf")
pdf_path = "../data/titanic_info.pdf"
titanic_pdf = PDFReader().load_data(file=pdf_path)
titanic_index = get_index(titanic_pdf, "titanic")
titanic_info_engine = titanic_index.as_query_engine()