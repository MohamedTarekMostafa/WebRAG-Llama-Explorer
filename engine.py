#this file is responsible for embedding splitters that i created in {processor.py}
from pyexpat import model
from langchain_huggingface import HuggingFaceEmbeddings
from dotenv import load_dotenv
import processor as poc
from langchain_groq import ChatGroq
from langchain_chroma import Chroma
from langchain_core.runnables import RunnablePassthrough
from langchain_core.prompts import ChatPromptTemplate,PromptTemplate
from langchain_core.output_parsers import StrOutputParser
load_dotenv(".env")

def get_rag_chain():
    splits = poc.get_split()
    chroma_db = './chroma_db'
    embeddings  = HuggingFaceEmbeddings(model_name='all-MiniLM-L6-v2')
    llm = ChatGroq(
        model = 'llama-3.3-70b-versatile',
        max_tokens = 512,
        temperature=0
    )
    vector_store = Chroma.from_documents(documents =splits,embedding=embeddings,persist_directory=chroma_db)
    retriever = vector_store.as_retriever()
    template = """استخدم قطع المعلومات التالية للإجابة على السؤال في النهاية.
    إذا كنت لا تعرف الإجابة، قل إنك لا تعرف، لا تحاول اختراع إجابة.
    استخدم ثلاث جمل كحد أقصى واجعل الإجابة مختصرة.

    Context: {context}
    Question: {question}
    Helpful Answer:"""
    
    prompt = PromptTemplate.from_template(template)
    def format_docs(docs):
        return f"\n".join(doc.page_content for doc in docs)
    rag_chain = ({"context":retriever|format_docs
                  ,"question":RunnablePassthrough()}|prompt|llm|StrOutputParser())
    return rag_chain




