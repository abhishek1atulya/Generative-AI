from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_core.prompts import ChatPromptTemplate


load_dotenv()

model = ChatGoogleGenerativeAI(model='gemini-1.5-pro')

chat_history = [SystemMessage('you are my helpful AI experts')]
while True:
    user_input = input('You: ')
    chat_history.append(HumanMessage(user_input))
    if user_input == 'exit':
        break
    result = model.invoke(chat_history)
    chat_history.append(AIMessage(result.content))
    print('AI:', result.content)
with open('chat_history.txt', 'w') as f:
    for i in chat_history:
        f.writelines(str(i))
print('Chat history:', chat_history)
