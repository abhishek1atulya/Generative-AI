from langchain_google_genai import GoogleGenerativeAI
from dotenv import load_dotenv
load_dotenv()
llm = GoogleGenerativeAI(model = 'gemini-1.5-pro')
result = llm.invoke("What is the meaning of life?")
print(result)