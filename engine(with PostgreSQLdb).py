import os
from langchain_huggingface import HuggingFaceEmbeddings
from dotenv import load_dotenv
import processor as poc
from langchain_groq import ChatGroq
from langchain_postgres.vectorstores import PGVector
from langchain_core.runnables import RunnablePassthrough
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv(".env")

def get_rag_chain():
    connection_string = 'postgresql+psycopg2://postgres:5822@localhost:5432/postgres_db'
    collection_name = "my_documents_collection"
    embeddings = HuggingFaceEmbeddings(model_name='all-MiniLM-L6-v2')
    
    llm = ChatGroq(
        model='llama-3.3-70b-versatile',
        max_tokens=512,
        temperature=0
    )

    vector_store = PGVector(
        connection=connection_string,
        collection_name=collection_name,
        embeddings=embeddings,
        use_jsonb=True
    )
    retriever = vector_store.as_retriever()
    
    template = """استخدم قطع المعلومات التالية للإجابة على السؤال في النهاية...
    Context: {context}
    Question: {question}
    Helpful Answer:"""
    
    prompt = PromptTemplate.from_template(template)
    
    def format_docs(docs):
        return "\n".join(doc.page_content for doc in docs)
    
    rag_chain = (
        {"context": retriever | format_docs, "question": RunnablePassthrough()}
        | prompt 
        | llm 
        | StrOutputParser()
    )
    
    return rag_chain