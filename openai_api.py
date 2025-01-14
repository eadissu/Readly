# File for managing the OpenAI API
# Reference: https://github.com/edenhandom/mood-mix/blob/main/util/openai_client.py
import os
from dotenv import load_dotenv
import openai

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

if not OPENAI_API_KEY:
    print("Failed to load API key. Check your .env file.")
else:
    print("API key loaded successfully!")

response = openai.ChatCompletion.create(
    model="gpt-4",  # You can also use "gpt-3.5-turbo" for lower cost
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "What is Python used for?"}
    ]
)

print("Response from ChatGPT:")
print(response["choices"][0]["message"]["content"])