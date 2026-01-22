from dotenv import load_dotenv
from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage
from typing import List, Dict, Any

from app.prompts.chat_prompt import get_chat_prompt
# from app.memory.in_memory import InMemoryChatStore



load_dotenv()
 
#---------------------- Sprint 1: Basic LLM Chat Service Implementation 
# llm = HuggingFaceEndpoint(
#     repo_id="HuggingFaceH4/zephyr-7b-beta",#"sequelbox/Llama2-70B-SunsetBoulevard"
#     task="text-generation",
#     max_new_tokens=300
# )

# model = ChatHuggingFace(llm=llm)

# memory =  InMemoryChatStore()


# def chat(session_id:str,domain:str,user_input:str)->str:
#     history = memory.get(session_id)

#     prompt = chat_prompt.invoke({
#         "domain":domain,
#         "user_input":user_input,
#         "history":history
#     })

#     response = model.invoke(prompt)
#     memory.add(session_id,user_input,response.content)

#     return response.content

#------------------------------------------ SPRINT-2 : Using Dynamic Prompts with Langchain---------------

class ChatService:
    """
    Service Layer responsible for:
    - Loading LLM
    - Applying prompt templates
    - Generating responses
    """

    def __init__(self):
        self.llm = HuggingFaceEndpoint(
            repo_id="mistralai/Mistral-7B-Instruct-v0.2",#"HuggingFaceH4/zephyr-7b-beta"
            task="text-generation",
            max_new_tokens=512
        )

        self.model = ChatHuggingFace(llm=self.llm)
        self.prompt = get_chat_prompt()

    def generate_response(
            self,
            user_message:str,
            chat_history:List=None
    )->str:
        """
        Generate LLM response based on user message and chat history.
        """

        if chat_history is None:
            chat_history = []
        
        try:
            formatted_prompt = self.prompt.invoke({
                "chat_history":chat_history,
                "user_message":user_message
            })
            response = self.model.invoke(formatted_prompt)
            return response.content
        except Exception as e:
            # in production this woule be logged to a monitoring service
            raise RuntimeError(f"Error generating LLM response: {str(e)}")
            