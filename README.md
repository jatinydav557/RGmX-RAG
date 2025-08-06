# 📕 Multi-PDF Chatbot with LangChain, Groq & Streamlit

A simple, interactive chatbot app built using **LangChain**, **HuggingFace embeddings**, **Groq's LLaMA 3 model**, and **Streamlit** that allows you to upload multiple PDF documents and ask questions using natural language. The chatbot retrieves relevant information using a vector database (Chroma) and maintains conversation history.

---

## ✨ Features

- 📄 Upload and chat with **multiple PDFs**
- 🧠 Contextual **chat history** across questions
- 💬 Uses **Groq’s LLaMA 3-70B-8192** for responses
- 🔍 Intelligent document retrieval with **Chroma Vector DB**
- ⚙️ Embedding with `sentence-transformers/all-MiniLM-L6-v2`
- 🚀 Simple and fast UI using **Streamlit**

---

## 📦 Installation

### 1. Clone the repository
```bash
git clone https://github.com/your-username/multi-pdf-chatbot.git
cd multi-pdf-chatbot
