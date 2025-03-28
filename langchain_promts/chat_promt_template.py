from langchain_core.prompts import ChatPromptTemplate

from langchain_core.messages import SystemMessage, HumanMessage, AIMessage

chat_template = ChatPromptTemplate([
    ('system', 'you are my helpful {domain} experts'),
    ('human', '{query}')
])

promt_template = chat_template.invoke({'domain': 'AI',
    'query': 'tell me about langchain in 50 words'
    })
print(promt_template)