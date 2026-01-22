from typing import Dict, List

class SessionManager:
    def __init__(self):
        # session_id -> list of messages
        self.sessions: Dict[str, List[str]] = {}

    def get_history(self, session_id: str) -> List[str]:
        return self.sessions.get(session_id, [])

    def append_message(self, session_id: str, message: str):
        if session_id not in self.sessions:
            self.sessions[session_id] = []
        self.sessions[session_id].append(message)
