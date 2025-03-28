from langchain_huggingface import HuggingFaceEmbeddings
from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
load_dotenv()
embedding = HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2')
documents = [
    "Delhi is the capital of India",
    "Kolkata is the capital of West Bengal",
    "Paris is the capital of France"
]
vector = embedding.embed_documents(documents)
query = "what is the capital of India"
query_vector = embedding.embed_query(query)
similarity = cosine_similarity([query_vector], vector)

index , value = max(enumerate(similarity[0]), key=lambda x: x[1])

print(f"Most similar document: {documents[index]}, similarity: {value}")

