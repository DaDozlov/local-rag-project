import streamlit as st
from ml.models.rag_model import rag_chain

st.title("Local RAG – DeepSeek‑R1")
query = st.chat_input("Ask something about your docs …")

if query:
    with st.spinner("Thinking…"):
        answer = rag_chain.invoke(query)
        st.markdown(answer.content)