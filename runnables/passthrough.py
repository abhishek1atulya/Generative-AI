from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate   
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
import os
from langchain.schema.runnable import RunnableSequence, RunnablePassthrough, RunnableParallel

load_dotenv()

model = ChatGoogleGenerativeAI(model='gemini-1.5-pro')

promt1 = PromptTemplate(template="What is the capital of {country}",
                        input_variables=["country"])
prompt2 = PromptTemplate(template="What is the population of {city} only provide the number",
                        input_variables=["city"])

parser = StrOutputParser()

chain = RunnableSequence(promt1, model, parser, prompt2, model, parser)

passthrough = RunnableParallel({'country': RunnablePassthrough(),
                            'capital': promt1 | model | parser,
                            'population': chain})
                                

passthrough_result = passthrough.invoke({"country": "USA"})

print(passthrough_result)

print(RunnablePassthrough().invoke('country'))

