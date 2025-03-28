from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
load_dotenv()

model = ChatGoogleGenerativeAI(model='gemini-1.5-pro', temperature=1)

result = model.invoke("write four line poem on love")

print(result.content)

