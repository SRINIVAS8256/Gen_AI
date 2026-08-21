from  langchain_huggingface import HuggingFacePipeline,ChatHuggingFace
from dotenv import load_dotenv

llm=HuggingFacePipeline.from_model_id(
    model_id="TinyLlama/TinyLlama_v1.1",
    task="text-generation",
    pipeline_kwargs=dict(
        temperature=1.9,
        max_new_tokens=512
    )
)

model =ChatHuggingFace(llm=llm)
result=model.invoke("tell me 5 dark meme about AI models")
print(result.content)