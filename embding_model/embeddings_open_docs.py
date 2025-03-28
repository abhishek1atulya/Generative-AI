from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
load_dotenv()
embedding = OpenAIEmbeddings(model='text-embedding-3-large', dimensions=32)
docs = ['Delhi is the capital of India', 
        'Mumbai is the financial capital of India',
        'India is a country in South Asia',
        'India is a democratic country',]
result = embedding.embed_documents(docs)

print(result)