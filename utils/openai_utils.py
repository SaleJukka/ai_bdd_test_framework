from openai import OpenAI # Import the OpenAI class from the openai module
from config.prompts import prompts # Import the prompts dictionary from the config.prompts module
import json # Import the json module

# Initialize the OpenAI client with the API key
def initialize_client():
    with open("config/openai_key.json", "r") as f:
        api_key = json.load(f)["api_key"]
    return OpenAI(api_key=api_key)

client = initialize_client() # Initialize the OpenAI client

def load_promt(key):
    """Retrieve the prompt from the prompts dictionary"""
    return prompts.get(key, "")

# Generate text using OpenAI
def generate_text(prompt):
    messages = [{"role": "user", "content": prompt}]
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=messages,
        max_tokens=700
    )
    return response.choices[0].message.content.strip()




