from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
import os
from langchain.schema.runnable import RunnableSequence

load_dotenv()

model = ChatGoogleGenerativeAI(model='gemini-1.5-pro')

promt1 = PromptTemplate(template="What is the capital of {country}",
                        input_variables=["country"])

promt2 = PromptTemplate(template="What is the population of {city}",
                        input_variables=["city"])
parser = StrOutputParser()

chain = RunnableSequence(promt1, model, parser, promt2, model, parser)
# we can also use the following chain
# chain = promt1 | model | parser | promt2 | model | parser

result = chain.invoke({"country": "USA"})

print(result)

