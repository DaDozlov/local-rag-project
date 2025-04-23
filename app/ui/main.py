import re
import streamlit as st
from typing import List
from ml.models.rag_model import rag_chain

st.title("Local RAG using DeepSeek")

query = st.chat_input("Ask something about your docs…")

if query:
    with st.spinner("Thinking…"):
        answer = rag_chain.invoke(query)

        raw_text: str = str(answer.content)

        THINK_RE: re.Pattern[str] = re.compile(
            r"<think>(.*?)</think>", re.DOTALL
        )

        think_blocks: List[str] = [
            blk.strip() for blk in THINK_RE.findall(raw_text)
        ]
        visible_text: str = THINK_RE.sub("", raw_text).strip()

    st.markdown(visible_text)

#    if think_blocks:
#        with st.expander("internal reasoning (click to view)"):
#            for block in think_blocks:
#                st.markdown(block)
