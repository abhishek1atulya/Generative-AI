from langchain_core.prompts import ChatPromptTemplate

# from langchain_core.utils import load_dotenv
# load_dotenv()

chat_promts = ChatPromptTemplate([('system','you are my helpful {domain} experts'),
                                ('human','how {topic} works')])
promts = chat_promts.invoke({'domain':'python', 'topic':'python list'})

print(promts)