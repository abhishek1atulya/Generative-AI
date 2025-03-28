from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

print('something')

client = OpenAI(api_key=OPENAI_API_KEY)

response = client.responses.create(
    model="gpt-4o-mini",
    input="tell me a joke",
)

print(response.output[0].content[0].text)