from engine import get_rag_chain
chain = get_rag_chain()
question = 'اذكرلي عشره لاعبين محترفين مصريين'
response = chain.invoke(question)
print(response)