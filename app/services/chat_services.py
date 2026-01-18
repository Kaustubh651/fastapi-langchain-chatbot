from dotenv import load_dotenv
from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from app.prompts.chat_prompt import chat_prompt
from app.memory.in_memory import InMemoryChatStore

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="HuggingFaceH4/zephyr-7b-beta",
    task="text-generation",
    max_new_tokens=300
)

model = ChatHuggingFace(llm=llm)

memory =  InMemoryChatStore()

def chat(session_id:str,domain:str,user_input:str)->str:
    history = memory.get(session_id)

    prompt = chat_prompt.invoke({
        "domain":domain,
        "user_input":user_input,
        "history":history
    })

    response = model.invoke(prompt)
    memory.add(session_id,user_input,response.content)

    return response.content