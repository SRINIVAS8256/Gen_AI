import langchain
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model=ChatOpenAI(model='gpt-4',temperature=0.5,max_tokens=1000)
result=model.invoke("whats the capital of india")
print(result)
print(result.content)