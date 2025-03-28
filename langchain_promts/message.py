from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage

load_dotenv()
model = ChatGoogleGenerativeAI(model='gemini-1.5-pro')

message = [SystemMessage('you are my helpful AI experts'),
           HumanMessage('tell me about langchain in 50 words')]
result = model.invoke(message)

print(result.content)

message.append(AIMessage(content=result.content))
print(message)