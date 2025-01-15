from flask import Flask
import os
from dotenv import load_dotenv
from gTTS_text_to_speech import generate_speech
from openai_api import OpenAIClient

# Load environment variables
load_dotenv()

app = Flask(__name__)

'''
    Get API Key
'''
def get_api_key():
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise ValueError("Failed to load API key. Check your .env file.")
    return api_key

OPENAI_API_KEY = get_api_key()

@app.route('/')
def index():
    """
    Main route that executes text-to-speech and speech-to-text functions.
    """
    # Generate speech
    audio_path = generate_speech(file_path="final_test2_output.mp3", play_audio=False)
    if not audio_path:
        return "Text-to-speech failed."

    # Transcribe speech
    openai_client = OpenAIClient(OPENAI_API_KEY)
    transcription = openai_client.transcribe(audio_path, transcription_path="transcription.txt")

    if transcription:
        return f"Transcription completed: {transcription}"
    else:
        return "Transcription failed."

if __name__ == '__main__':
    app.run(debug=True)
