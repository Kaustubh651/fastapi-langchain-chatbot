from langchain_core.prompts import ChatPromptTemplate, SystemMessagePromptTemplate, HumanMessagePromptTemplate, AIMessagePromptTemplate
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage  


chat_prompt = ChatPromptTemplate.from_messages([
    ("system","You are a helpful {domain} expert."),
    ("human","{user_input}")
])