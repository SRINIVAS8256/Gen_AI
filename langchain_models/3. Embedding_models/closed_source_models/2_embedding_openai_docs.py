from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
load_dotenv()

embedding=OpenAIEmbeddings(model="text-embedding-3-large",dimensions=32)
documents=["whats the weather like in New York City today?"
           ,"whats the weather like in Los Angeles today?"
           ,"whats the weather like in Chicago today?"]
result=embedding.embed_documents(documents)
print(str(result))
print(str(len(result)))