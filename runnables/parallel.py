from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
import os
from langchain.schema.runnable import RunnableSequence, RunnableParallel

load_dotenv()

model = ChatGoogleGenerativeAI(model='gemini-1.5-pro')

prompt1 = PromptTemplate(template = 'what is the capital of {country1} and {country2}',
                         input_variables = ['country1','country2'])

prompt2 = PromptTemplate(template = 'what is the population of {city} only provide the number',
                         input_variables = ['city'])

parser1 = StrOutputParser()

parallel = RunnableParallel({
    "country": prompt1 | model | parser1,
    "population": prompt2 | model | parser1
})

parallel_result = parallel.invoke({"country1": "USA", 'country2': "india", "city": "New York"})

print(parallel_result)
