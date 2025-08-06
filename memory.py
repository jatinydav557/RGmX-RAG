from langchain.chains import ConversationalRetrievalChain
from langchain_groq import ChatGroq
from langchain.vectorstores import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from langchain.memory import ConversationBufferMemory
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()
api_key = os.getenv("GROQ_API_KEY")

# Initialize the embedding model
embeddings = HuggingFaceEmbeddings(model="sentence-transformers/all-MiniLM-L6-v2")

# Initialize the LLM globally
llm = ChatGroq(
    api_key=api_key,
    model='llama3-70b-8192'
)

def get_chain():
    # Load persisted vector DB
    vectorstore = Chroma(
        persist_directory="Chroma_db",
        embedding_function=embeddings
    )

    # Create retriever
    retriever = vectorstore.as_retriever(search_type="similarity", search_kwargs={"k": 1})

    # Setup memory
    memory = ConversationBufferMemory(
        memory_key="chat_history",
        return_messages=True
    )

    # ⬅️ Tell memory which output key to store
    memory.output_key = "answer"

    # Create ConversationalRetrievalChain
    qa_chain = ConversationalRetrievalChain.from_llm(
        llm=llm,
        retriever=retriever,
        memory=memory,
        return_source_documents=True,
        output_key="answer"
    )

    return qa_chain
