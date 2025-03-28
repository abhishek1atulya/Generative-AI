from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
from typing import Optional

load_dotenv()


model = ChatGoogleGenerativeAI(model='gemini-1.5-pro')


class person(BaseModel):
    name: str = Field(..., description='Name of the person')
    age: int = Field(gt=18, description='Age of the person')
    occupation: str = Field(..., description='Occupation of the person')
    location: str = Field(..., description='home city of the person')
    email: Optional[str] = Field(None, description='Email of the person')

parser = PydanticOutputParser(pydantic_object=person)

template = PromptTemplate(
    template='provide the detailed information of a {nationality} cricket player\n{format_output}',
    input_variables=['nationality'],
    partial_variables={'format_output': parser.get_format_instructions()}
)

chain = template | model | parser

result = chain.invoke({'nationality':'Indian'})

print(result)