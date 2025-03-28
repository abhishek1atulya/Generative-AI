from langchain_community.document_loaders import TextLoader
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_community.vectorstores import FAISS, Chroma
from dotenv import load_dotenv
from langchain_huggingface import HuggingFaceEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_core.prompts import ChatPromptTemplate, PromptTemplate
from langchain.chains import create_retrieval_chain

load_dotenv()

# load the embedding model
embedding_model = HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2')

# Load the model
llm = ChatGoogleGenerativeAI(model='gemini-1.5-pro')
# Load a single text file
loader = TextLoader(r"documents/state_of_the_union.txt",encoding="utf-8")

documents = loader.load()

text_spliter = RecursiveCharacterTextSplitter(chunk_size=500,
    chunk_overlap=50,
    separators=["\n\n", "\n", " "])

chuncks = text_spliter.split_documents(documents)

vector_db = Chroma.from_documents(chuncks, embedding_model)

retriver = vector_db.as_retriever(search_type = 'similarity', search_kwargs= {'k':3})

# query = PromptTemplate(template='tell me about {topic}',
#                        input_variables= 'topic')
# query = query.invoke('putin')
query = 'tell me about putin'

relevent_docs = retriver.get_relevant_documents(query)

# print('relevent_docs: ', relevent_docs)

context = ' '.join([doc.page_content for doc in relevent_docs])

prompt = f'{context} \non the basis of above context answer the {query}'

response = llm.invoke(prompt)

# Output
print("Response:", response.content)





