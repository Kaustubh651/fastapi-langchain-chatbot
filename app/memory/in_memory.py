from collections import defaultdict
from langchain_core.messages import HumanMessage, AIMessage

class InMemoryChatStore:
    def __init__(self):
        self.store = defaultdict(list)

    def get(self,session_id):
        return self.store[session_id]
    
    def add(self,session_id,human,ai):
        self.store[session_id].append(HumanMessage(content=human))
        self.store[session_id].append(AIMessage(content=ai))