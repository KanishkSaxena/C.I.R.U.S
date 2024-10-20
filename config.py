from langchain.globals import set_llm_cache
from langchain.cache import InMemoryCache
from dotenv import load_dotenv
import os

load_dotenv()

set_llm_cache(InMemoryCache())

import openai

openai.api_key = os.getenv("API_KEY")

def generate_response(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo", 
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    return response['choices'][0]['message']['content']