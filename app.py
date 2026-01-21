import streamlit as st
from llm import load_llm
from retriever import get_context

st.set_page_config(page_title="Jarvis AI")

st.title("🤖 Jarvis – Personal AI Assistant")

llm = load_llm()

query = st.text_input("Ask Jarvis:")

if query:
    context = get_context(query)

    prompt = f"""
Context:
{context}

Question:
{query}

Answer:
"""

    response = llm(prompt, max_length=200, do_sample=True)
    st.write(response[0]["generated_text"])
