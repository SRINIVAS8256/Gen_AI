from langchain_huggingface import HuggingFaceEmbeddings

embedding = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
text="delhi is the capital of india"
vector=embedding.embed_query(text)
documents=["whats the weather like in New York City today?"
           ,"whats the weather like in Los Angeles today?"
           ,"whats the weather like in Chicago today?"]
vector_doc=embedding.embed_documents(documents)
print(str(vector))
print("\n")
print(str(vector_doc))