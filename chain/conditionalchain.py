from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser, PydanticOutputParser
from langchain.schema.runnable import RunnableLambda, RunnableBranch
from pydantic import BaseModel, Field
from typing import Optional, Literal

model = ChatGoogleGenerativeAI(model='gemini-1.5-pro')

class FeedBack(BaseModel):
    sentiment: Literal['positive', 'negative', 'neutral'] = Field(..., description='Feedback on the generated content')

parser1 = PydanticOutputParser(pydantic_object=FeedBack)

parser2 = StrOutputParser()

template1 = PromptTemplate(template = 'classfy the following feedback as positive, negative, neutral, this is not feedback \n{feedback}\n{format_output}',
                            input_variables=['feedback'],
                            partial_variables={'format_output': parser1.get_format_instructions()})
template2 = PromptTemplate(template='write the apropraite response for the positive feedback in 2 line\n{feedback}',
                          input_variables=['feedback'])
                          
template3 = PromptTemplate(template='write the apropraite response for the negative feedback in 2 line\n{feedback}',
                          input_variables=['feedback'])   
 
template4 = PromptTemplate(template='write the apropraite response for the neutral feedback in 2 line\n{feedback}',
                          input_variables=['feedback'])

chain = RunnableBranch(
    (lambda x : x.sentiment == 'positive', template2 | model | parser2),
    (lambda x : x.sentiment == 'negative', template3 | model | parser2),
    (lambda x : x.sentiment == 'neutral', template4 | model | parser2),
    RunnableLambda(lambda x: 'could not classify the feedback')
) 

FeedBack = template1 | model | parser1 | chain

print(FeedBack.invoke({'feedback':'I am busy I will call you later'}))

chain.get_graph().print_ascii()

                 
