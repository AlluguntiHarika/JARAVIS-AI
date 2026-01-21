import os
import streamlit as st
from pinecone import Pinecone
from sentence_transformers import SentenceTransformer

# -------------------------------------------------
# STREAMLIT PAGE CONFIG (MUST BE FIRST)
# -------------------------------------------------
st.set_page_config(
    page_title="Jarvis AI Assistant",
    page_icon="🤖",
    layout="centered"
)

st.title("🤖 Jarvis AI Assistant")

# -------------------------------------------------
# LOAD API KEY FROM ENVIRONMENT
# -------------------------------------------------
PINECONE_API_KEY = "pcsk_2wRURV_8h2RUrbr74q2sYkGcuR5La17QAS2Ln7uxjXxCkTZwcxao9ZwhhaEQjce8AYZCSf"


if not PINECONE_API_KEY:
    st.error("❌ PINECONE_API_KEY environment variable not set")
    st.info("Run this in PowerShell:\n\nsetx PINECONE_API_KEY \"YOUR_API_KEY\"\n\nThen restart terminal.")
    st.stop()

# -------------------------------------------------
# LOAD MODELS & PINECONE (CACHED)
# -------------------------------------------------
@st.cache_resource
def load_resources():
    embed_model = SentenceTransformer("all-MiniLM-L6-v2")
    pc = Pinecone(api_key=PINECONE_API_KEY)
    index = pc.Index("jarvis-index")
    return embed_model, index

embed_model, index = load_resources()

# -------------------------------------------------
# CHAT SESSION STATE
# -------------------------------------------------
if "messages" not in st.session_state:
    st.session_state.messages = []

# Render previous messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# -------------------------------------------------
# USER INPUT
# -------------------------------------------------
user_input = st.chat_input("Ask Jarvis something...")

if user_input:
    # Show user message
    st.session_state.messages.append(
        {"role": "user", "content": user_input}
    )
    with st.chat_message("user"):
        st.markdown(user_input)

    # -------------------------------------------------
    # RETRIEVE MEMORY FROM PINECONE
    # -------------------------------------------------
    query_embedding = embed_model.encode(user_input).tolist()

    results = index.query(
        vector=query_embedding,
        top_k=3,
        include_metadata=True
    )

    context = "\n".join(
        [match["metadata"]["text"] for match in results["matches"]]
    )

    if not context:
        context = "No relevant memory found."

    response = f"""
### 🧠 Jarvis Memory
{context}
"""

    # Show assistant response
    st.session_state.messages.append(
        {"role": "assistant", "content": response}
    )
    with st.chat_message("assistant"):
        st.markdown(response)
