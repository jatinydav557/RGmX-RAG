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

2. Create a virtual environment

python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

3. Install dependencies

pip install -r requirements.txt

🔑 Environment Variables

Create a .env file in the project root with your Groq API key:

GROQ_API_KEY=your_groq_api_key_here

🚀 Running the App

streamlit run app.py

Then open your browser at: http://localhost:8501
📁 Project Structure

multi-pdf-chatbot/
│
├── app.py                   # Streamlit UI
├── ingestion.py             # PDF loader + vector DB creation
├── memory.py                # QA chain with Groq + LangChain memory
├── uploads/                 # Uploaded PDFs
├── Chroma_db/               # Vector DB (auto-generated)
├── .env                     # Environment file (not committed)
└── requirements.txt         # Dependencies

📸 Screenshot

🙋‍♂️ How it Works

    Upload one or more PDF files.

    The app loads and splits them into chunks using RecursiveCharacterTextSplitter.

    Embeddings are generated using HuggingFace MiniLM.

    The chunks are stored in Chroma vector DB.

    Your questions are passed to ConversationalRetrievalChain which:

        Retrieves relevant chunks

        Sends them to Groq's LLaMA 3

        Maintains chat memory

    You get contextual and accurate answers with source chunks shown.

📚 Technologies Used

    LangChain

    Groq LLaMA 3

    HuggingFace Sentence Transformers

    Chroma Vector Store

    Streamlit

📝 License

MIT License. Feel free to fork and improve!
🤝 Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.
👨‍💻 Author

Jatin – AI & LLM Enthusiast
📧 [Your email]
🔗 LinkedIn • GitHub
