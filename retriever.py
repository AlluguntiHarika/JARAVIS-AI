from pinecone import Pinecone
from sentence_transformers import SentenceTransformer

# ----------------------------
# CONFIG
# ----------------------------
API_KEY = "pcsk_2wRURV_8h2RUrbr74q2sYkGcuR5La17QAS2Ln7uxjXxCkTZwcxao9ZwhhaEQjce8AYZCSf"
INDEX_NAME = "jarvis-index"
TOP_K = 3

# ----------------------------
# INIT
# ----------------------------
pc = Pinecone(api_key=API_KEY)
index = pc.Index(INDEX_NAME)

model = SentenceTransformer("all-MiniLM-L6-v2")

# ----------------------------
# QUERY
# ----------------------------
query = input("Ask Jarvis something: ")

query_embedding = model.encode(query).tolist()

results = index.query(
    vector=query_embedding,
    top_k=TOP_K,
    include_metadata=True
)

print("\n🔍 Relevant Memory:")
for match in results["matches"]:
    print(f"- {match['metadata']['text']}")
