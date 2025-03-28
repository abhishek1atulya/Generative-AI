# from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
import json
load_dotenv()

# llm = HuggingFaceEndpoint(
#     repo_id="google/gemma-2-2b-it",
#     task="text-generation"
# )
# model = ChatHuggingFace(llm=llm)

model = ChatGoogleGenerativeAI(model='gemini-1.5-pro')

parser = JsonOutputParser()

template = PromptTemplate(
    template='Give me 5 fact about the {topic} \n{format_output}',
    input_variables=['topic'],
    partial_variables={'format_output': parser.get_format_instructions()}

)
prompt = template.invoke({'topic':'sun'})
# print(prompt)

t = PromptTemplate(
    template='Give me 5 fact about the sun \n{format_output}',
    partial_variables={'format_output': parser.get_format_instructions()})

p = t.format()
# print(p)

result = model.invoke(p)

# print(result)

jason_result  = parser.parse(result.content)

# print(jason_result)

chain = template | model | parser

result = chain.invoke({'topic':'sun'})

print(result)

