from langchain_community.chat_models import ChatOllama
from langchain.prompts import ChatPromptTemplate
from langchain.schema.runnable import RunnableParallel, RunnablePassthrough
from ml.pipelines.retriever import build_retriever

_llm = ChatOllama(model="deepseek-r1")
_retriever = build_retriever()
_prompt = ChatPromptTemplate.from_template(
    """Answer the question using the context. Cite source metadata.
    Question: {question}\nContext: {docs}"""
)

rag_chain = RunnableParallel(
    {"question": RunnablePassthrough(), "docs": _retriever}
) | _prompt | _llm