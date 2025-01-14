# File for managing the OpenAI API
# Reference: https://github.com/edenhandom/mood-mix/blob/main/util/openai_client.py
import os
from dotenv import load_dotenv
import openai

# Load environment variables from .env file
load_dotenv()

# Get the API key from the environment
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

if not OPENAI_API_KEY:
    print("Failed to load API key. Check your .env file.")
else:
    print("API key loaded successfully!")

# Explicitly set the API key for the OpenAI library
openai.api_key = OPENAI_API_KEY

# Call OpenAI's ChatCompletion API
try:
    response = openai.ChatCompletion.create(
        model="gpt-4",  # You can also use "gpt-3.5-turbo" for lower cost
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "What is Python used for?"}
        ]
    )

    print("Response from ChatGPT:")
    print(response["choices"][0]["message"]["content"])

except openai.error.AuthenticationError:
    print("Authentication failed: Check your API key.")
except Exception as e:
    print(f"An error occurred: {e}")
