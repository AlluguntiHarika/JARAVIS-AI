from pinecone import Pinecone, ServerlessSpec
from sentence_transformers import SentenceTransformer

# Initialize Pinecone (NEW WAY)
pc = Pinecone(
    api_key="pcsk_2wRURV_8h2RUrbr74q2sYkGcuR5La17QAS2Ln7uxjXxCkTZwcxao9ZwhhaEQjce8AYZCSf"
)

index_name = "jarvis-index"

# Create index if not exists
existing_indexes = [idx.name for idx in pc.list_indexes()]

if index_name not in existing_indexes:
    pc.create_index(
        name=index_name,
        dimension=384,
        metric="cosine",
        spec=ServerlessSpec(
            cloud="aws",
            region="us-east-1"
        )
    )

index = pc.Index(index_name)

model = SentenceTransformer("all-MiniLM-L6-v2")

with open("data/company_docs.txt", "r", encoding="utf-8") as f:
    text = f.read()

embedding = model.encode(text).tolist()

index.upsert([
    {
        "id": "doc1",
        "values": embedding,
        "metadata": {"text": text}
    }
])

print("✅ Data successfully stored in Pinecone")
