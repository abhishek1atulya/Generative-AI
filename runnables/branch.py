from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
import os
from langchain.schema.runnable import RunnableSequence, RunnableLambda, RunnablePassthrough, RunnableParallel, RunnableBranch

load_dotenv()

model = ChatGoogleGenerativeAI(model='gemini-1.5-pro')

parser = StrOutputParser()

prompt1 = PromptTemplate(
    template='Write a detailed report on {topic}',
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template='Summarize the following text \n {text}',
    input_variables=['text']
)

chain1 = prompt1 | model | parser

branch = RunnableBranch(
    (lambda x: len(x.split())>300 , prompt2 | model | parser),
    RunnablePassthrough()
)

final_chain = RunnableSequence(chain1, branch)

result = final_chain.invoke({'topic': 'AI'})

print(result)