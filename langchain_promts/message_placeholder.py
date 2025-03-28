from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

from langchain_google_genai import ChatGoogleGenerativeAI

model = ChatGoogleGenerativeAI(model='gemini-1.5-pro')

chat_template = ChatPromptTemplate([
                                    ('system','you are my helpful {domain} experts'),
                                  MessagesPlaceholder(variable_name= 'chat_history'),
                                  ('human','{query}')
                                  ])
chat_history = []
with open('chat_history.txt') as f:
    chat_history.extend(f.readlines())

# print('previous_chat_history: \n', chat_history)

# create prompt
prompt = chat_template.invoke({'domain': 'AI', 'chat_history':chat_history, 'query':'now multiply the last two numbers'})

# print('promt: \n',prompt)

result = model.invoke(prompt)

print('result: \n', result.content)
