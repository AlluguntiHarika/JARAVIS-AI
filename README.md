Jarvis AI Assistant

Jarvis AI Assistant is a Jarvis-style conversational AI system built using Python, Streamlit, Pinecone, and sentence-transformer embeddings.
The project demonstrates a Retrieval-Augmented Generation (RAG) pipeline with long-term memory and an interactive chat interface.


Tech Stack

Programming Language: Python

Frontend: Streamlit

Vector Database: Pinecone

Embeddings: sentence-transformers (all-MiniLM-L6-v2)

Architecture: RAG (Retrieval-Augmented Generation)



Setup Instructions
1. Clone the Repository
git clone https://github.com/<your-username>/jarvis-ai.git
cd jarvis-ai

2. Create and Activate Virtual Environment (Windows)
python -m venv venv
venv\Scripts\activate

3. Install Dependencies
pip install -r requirements.txt


If requirements.txt is not present, install manually:

pip install streamlit pinecone sentence-transformers torch

4. Set Pinecone API Key (Required)

Run this once in PowerShell:

setx PINECONE_API_KEY "YOUR_PINECONE_API_KEY"


Close and reopen PowerShell after setting the key.

Verify:

echo $Env:PINECONE_API_KEY

Usage
1. Ingest Data into Pinecone
python ingest.py


This creates the index (if not present) and stores document embeddings.

2. Test Retrieval (Optional)
python retriever.py


Enter a query to verify semantic search.

3. Run Chat Interface
streamlit run chat.py


Open the browser at:

http://localhost:8501


Results:<img width="1918" height="1152" alt="image" src="https://github.com/user-attachments/assets/d5ec1a47-c049-4c01-a725-172aeea34c41" />

Author

Harika Allugunti
