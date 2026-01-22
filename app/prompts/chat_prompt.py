from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage  


def get_chat_prompt():
    """
    Return a dyanamic chat prompt templete for LLM interactions.
    """
    system_message = SystemMessage(
        content=    ("You are a helpful AI assistant that provides accurate and concise information to users based on their queries."
        "If you don't know the answer, respond with 'I don't know' instead of making up information.") 
        
    )

    prompt = ChatPromptTemplate.from_messages([
        system_message,
        MessagesPlaceholder(variable_name="chat_history"),
        ("human","{user_message}"),
    ])
    return prompt