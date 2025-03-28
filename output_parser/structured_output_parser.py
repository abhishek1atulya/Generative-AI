from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain.output_parsers import StructuredOutputParser, ResponseSchema
from langchain_core.prompts import PromptTemplate

load_dotenv()

# llm = HuggingFaceEndpoint(
#     repo_id="TinyLlama/TinyLlama-1.18-Chat-v1.0",
#     task="text-generation"
# )
# model = ChatHuggingFace(llm=llm)

model = ChatGoogleGenerativeAI(model='gemini-1.5-pro')

schema = [ResponseSchema(name = 'fact1', description = 'fact1 about the topic',),
            ResponseSchema(name = 'fact2', description = 'fact2 about the topic',),
            ResponseSchema(name = 'fact3', description = 'fact3 about the topic',),
            ResponseSchema(name = 'fact4', description = 'fact4 about the topic',),
            ResponseSchema(name = 'fact5', description = 'fact5 about the topic',)]

parser = StructuredOutputParser.from_response_schemas(schema)

template = PromptTemplate(
    template='Give me 5 fact about the {topic}\n{format_output}',
    input_variables=['topic'],
    partial_variables={'format_output': parser.get_format_instructions()}
)

chain = template | model | parser

result = chain.invoke({'topic':'sun'})

print(result)