from langchain_core.messages import HumanMessage, AIMessage
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from app.core.session_manager import SessionManager
from dotenv import load_dotenv

load_dotenv()


class ChatService:
    def __init__(self):
        self.llm = ChatHuggingFace(
            llm=HuggingFaceEndpoint(
                repo_id="MiniMaxAI/MiniMax-M2.1",
                task="text-generation",
            )
        )

        self.session_manager = SessionManager()

    def generate_response(self, session_id: str, user_message: str) -> str:
        """
        Generate response using session-based conversation memory
        """

        # 1️⃣ Fetch history
        history = self.session_manager.get_history(session_id)

        # 2️⃣ Convert to LangChain messages
        messages = []
        for msg in history:
            if msg.startswith("USER:"):
                messages.append(HumanMessage(content=msg.replace("USER:", "")))
            else:
                messages.append(AIMessage(content=msg.replace("AI:", "")))

        # 3️⃣ Add new user message
        messages.append(HumanMessage(content=user_message))

        # 4️⃣ Call LLM
        response = self.llm.invoke(messages)

        ai_response = response.content

        # 5️⃣ Save conversation
        self.session_manager.append_message(session_id, f"USER:{user_message}")
        self.session_manager.append_message(session_id, f"AI:{ai_response}")

        return ai_response
