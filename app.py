import streamlit as st
from ingestion import create_vectorstore_from_pdf
from memory import get_chain
import os

st.set_page_config(page_title="📕 Multi-PDF Personal Chatbot")
st.title("📕 Multi-PDF Chatbot with Context History and Vector Database")

uploaded_files = st.file_uploader(
    "Upload PDF files", type=["pdf"], accept_multiple_files=True
)

if uploaded_files:
    file_paths = []
    for uploaded_file in uploaded_files:
        file_path = os.path.join("uploads", uploaded_file.name)
        os.makedirs("uploads", exist_ok=True)
        with open(file_path, "wb") as f:
            f.write(uploaded_file.getbuffer())
        file_paths.append(file_path)

    st.success("😄 Vector Database is ready,wait for a wile before querying.....")
    create_vectorstore_from_pdf(file_paths)

    chain = get_chain()

    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    user_input = st.text_input("You are ready to go!!! Ask me anything from uploaded files!!")
    if user_input:
        with st.spinner("Generating the answer..."):
            result = chain({"question": user_input})
            answer = result["answer"]
            sources = result.get("source_documents", [])

            st.session_state.chat_history.append(("You", user_input))
            st.session_state.chat_history.append(("LLM", answer, sources))

    for entry in st.session_state.chat_history:
        if entry[0] == "You":
            st.markdown(f"**🧑 You:** {entry[1]}")
        else:
            st.markdown(f"**🤖 LLM:** {entry[1]}")
            if entry[2]:
                with st.expander("📄 Context used from PDFs"):
                    for i, doc in enumerate(entry[2]):
                        st.markdown(f"**Chunk {i+1}:** {doc.page_content}")
