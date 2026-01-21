from transformers import pipeline

def load_llm():
    llm = pipeline(
        "text-generation",
        model="gpt2"
    )
    return llm
