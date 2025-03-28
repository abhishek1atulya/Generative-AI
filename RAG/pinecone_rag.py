from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS, Pinecone
from langchain.chains import RetrievalQA
from pinecone import Pinecone
from pinecone.grpc import PineconeGRPC as Pinecone
from langchain_google_genai import GoogleGenAI
from langchain_openai import OpenAI
from pinecone import ServerlessSpec
from dotenv import load_dotenv
import os

load_dotenv()

pinecone_api_key = os.getenv("PINECONE_API_KEY")

pc = Pinecone(api_key=pinecone_api_key)

pc = Pinecone(api_key="YOUR_API_KEY")

pc.create_index(
  name="example-index",
  dimension=1536,
  metric="cosine",
  spec=ServerlessSpec(
    cloud="aws",
    region="us-east-1"
  )
)