# File for managing the OpenAI API
# Reference: https://github.com/edenhandom/mood-mix/blob/main/util/openai_client.py
# OpenAi api key: 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
import os
from dotenv import load_dotenv

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

if not OPENAI_API_KEY:
    print("Failed to load API key. Check your .env file.")
else:
    print("API key loaded successfully!")