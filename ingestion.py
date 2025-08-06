from langchain_community.document_loaders import PyPDFLoader
from langchain_community.vectorstores import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter

embeddings = HuggingFaceEmbeddings(model="sentence-transformers/all-MiniLM-L6-v2")

def create_vectorstore_from_pdf(pdf_files):
    all_texts = []
    for file_path in pdf_files:
        loader = PyPDFLoader(file_path)
        docs = loader.load()
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=70)
        texts = text_splitter.split_documents(docs)
        all_texts.extend(texts)

    # ✅ Remove duplicate chunks using content as key
    unique_docs = list({doc.page_content: doc for doc in all_texts}.values())

    vectordb = Chroma.from_documents(
        documents=unique_docs,
        embedding=embeddings,
        persist_directory="Chroma_db"
    )

    # print("✅ Vector DB updated.")  #This was to test the py script
