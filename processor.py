#this file is responsible for splitting and preparation data to embedding model
import langchain
from langchain_community.document_loaders import WikipediaLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

def get_split():
    loader = WikipediaLoader(
        query='قائمة لاعبي كرة القدم المصريين في الدوريات الأجنبية',
        lang='ar',
        load_max_docs=1
    )
    docs = loader.load()
    splitter = RecursiveCharacterTextSplitter(
        chunk_size = 512,
        chunk_overlap = 50,
        length_function = len,
        is_separator_regex=False

    )
    splits = splitter.split_documents(docs)
    return splits
