# 🤖 LLM Chatbot API (FastAPI + Hugging Face)

A **production-ready chatbot backend** built using **FastAPI**, **Hugging Face LLMs**, and **dynamic prompt templates**.
Designed with **clean architecture**, **service separation**, and **agile sprint-based development**, similar to how real-world AI teams build systems.

---

## 📌 Project Overview

This project implements a **scalable chatbot API** that:

* Uses **Hugging Face LLMs** for text generation
* Supports **dynamic prompt templates**
* Is structured for **production deployment**
* Can be extended with **chat history, memory, embeddings, and RAG**

The goal is to build a **real AI backend**, not a demo script.

---

## 🧠 Key Features

* ✅ FastAPI-based REST API
* ✅ Modular & scalable folder structure
* ✅ Dynamic chat prompt templates
* ✅ Hugging Face model integration
* ✅ Clean service-layer architecture
* ✅ Swagger UI for API testing
* 🚧 Chat history & memory (Sprint 3)
* 🚧 RAG & vector database (future)

---

## 🏗️ Tech Stack

| Layer           | Technology                       |
| --------------- | -------------------------------- |
| API Framework   | FastAPI                          |
| LLM             | Hugging Face                     |
| Prompting       | LangChain-style prompt templates |
| Server          | Uvicorn                          |
| Environment     | Python 3.10+                     |
| Version Control | Git + GitHub                     |

---

## 📂 Project Structure

```
chatbot-api/
│
├── app/
│   ├── api/
│   │   └── chat.py          # Chat API endpoints
│   │
│   ├── services/
│   │   └── chat_service.py  # LLM interaction logic
│   │
│   ├── prompts/
│   │   └── chat_prompt.py  # Prompt templates
│   │
│   ├── schemas/
│   │   └── chat.py         # Request & response models
│   │
│   ├── core/
│   │   └── config.py       # Environment & settings
│   │
│   └── main.py             # FastAPI app entry point
│
├── .env                    # Environment variables
├── requirements.txt
├── README.md
└── run.sh / run.ps1
```

This structure follows **industry best practices** for AI backends.

---

## 🚀 Getting Started

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/chatbot-api.git
cd chatbot-api
```

---

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
```

Activate it:

**Windows**

```bash
venv\Scripts\activate
```

**Mac/Linux**

```bash
source venv/bin/activate
```

---

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4️⃣ Configure Environment Variables

Create a `.env` file:

```env
HUGGINGFACEHUB_API_TOKEN=your_hf_token_here
```

---

### 5️⃣ Run the Server

```bash
uvicorn app.main:app --reload
```

Server will start at:

```
http://127.0.0.1:8000
```

---

## 📘 API Documentation

Swagger UI:

```
http://127.0.0.1:8000/docs
```

---

## 💬 Chat API

### Endpoint

```
POST /api/v1/chat
```

### Request Body

```json
{
  "session_id": "abc123",
  "message": "What is LBW in cricket?"
}
```

### Response

```json
{
  "session_id": "abc123",
  "answer": "LBW stands for Leg Before Wicket..."
}
```

---

## 🧩 Prompt Design (Concept)

The chatbot uses **dynamic prompt templates**:

```
System: You are a helpful AI assistant.
User: {user_message}
Assistant:
```

This allows:

* Persona control
* Domain-specific behavior
* Easy prompt updates without touching API logic

---

## 🧪 Sprint-Based Development

### ✅ Sprint 1 – Project Foundation (Completed)

* Architecture design
* Tech stack selection
* Folder structure
* README & documentation

### 🚧 Sprint 2 – Core Chat API (In Progress)

* FastAPI endpoints
* Hugging Face integration
* Dynamic prompt handling

### 🔜 Sprint 3 – Chat Memory

* Message history
* Session-based conversations

### 🔜 Sprint 4 – RAG & Embeddings

* Vector database
* Document-based Q&A

---

## 🛡️ Production Readiness

Planned improvements:

* Centralized logging
* Rate limiting
* Async model calls
* Dockerization
* CI/CD pipeline
* API authentication

---

## 🎯 Why This Project Matters

This project demonstrates:

* Real-world **AI backend design**
* **Prompt engineering** in production
* Clean separation of concerns
* Agile sprint methodology
* Readiness for **enterprise-scale AI systems**

Perfect for:

* AI Engineer roles
* Backend + LLM positions
* Startup or enterprise AI teams

---

## 📄 License

MIT License

---

## 👤 Author

**Kaustubh Dwivedi**
AI / Backend Engineer
🚀 Building production-grade AI systems

