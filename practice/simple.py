from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain.schema.runnable import RunnableLambda, RunnablePassthrough, RunnableParallel
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage

load_dotenv()

model = ChatGoogleGenerativeAI(model='gemini-1.5-pro')

parser = StrOutputParser()


basic_prompt = PromptTemplate(template="Your an AI Assistant, I have to write a report on the patient. by asking the user the following questions: \n 1. What is the name of the patient? \n 2. What is the id of the patient? \n 3. What is the address of the patient? \n 4. What is the id of the doctor? \n 5. What is the diagnosis of the patient? \n 6. What is the treatment given to the patient?, please ask a quention at a time on the basis of these  chat_history {chat_history}",
                              input_variables=["chat_history"])

data_retrieval = PromptTemplate(template='please provide only name of the topic that is asked in the question \n {question}',
                              input_variables=["question"])

data = {}
chat_history=[]
c=0             
while True:
    chain = basic_prompt | model | parser
    result = chain.invoke({"chat_history":chat_history})
    field_chain = data_retrieval | model | parser
    print(result)
    n = input()
    field_chain = field_chain.invoke({"question":result})
    data[field_chain] = n
    chat_history.append(AIMessage(content=result))
    chat_history.append(HumanMessage(content=n))
    c+=1
    if c==6:
        break
    
promt_final = PromptTemplate(template="Write a detailed report on {data}",
                         input_variables=["data"])

resulting_chain = promt_final | model | parser

result = resulting_chain.invoke({"data":data})

print(result)





