# Reference: https://github.com/edenhandom/mood-mix/blob/main/app.py

"""
This main purpose of this file is to run the app. Call the backend things which include
openA
"""
from flask import Flask, render_template, request, jsonify, send_file
from gtts import gTTS
import os
from io import BytesIO
import openai
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route('/', methods=['GET', 'POST'])
def index():

    action = None
    # Get the sentence

    # Get the word
    word = "Test"
    

    # Listening for button click
    if request.method == 'POST':
        action = request.form.get('action')

    if action == "listen":
        print("Word:" + word)
    

    return render_template('index.html', content = word)

@app.route('/listen')
def listen():
    word = "dog"
    tts = gTTS(text=word, lang='en')
    audio_file = BytesIO()
    tts.write_to_fp(audio_file)
    audio_file.seek(0)
    return send_file(audio_file, mimetype='audio/mp3')

@app.route('/upload', methods=['POST'])
def upload():
    if 'audio_data' not in request.files:
        return jsonify({"error": "No audio file provided"}), 400

    audio_file = request.files['audio_data']
    audio_file.save('recorded_audio.wav')

    with open('recorded_audio.wav', 'rb') as audio:
        response = openai.Audio.transcribe(model="whisper-1", file=audio)

    transcription = response.get("text", "").strip().lower()
    target_word = "dog"

    if transcription == target_word:
        result = "Correct!"
    else:
        result = f"Incorrect. You said: {transcription}"

    return jsonify({"result": result})

if __name__ == '__main__':
    app.run(debug=True)

'''
from flask import (Flask, render_template)
import os
from dotenv import load_dotenv
from gTTS_text_to_speech import generate_speech
from openai_api import OpenAIClient
from database import db, Word, populate_database


# Load environment variables
load_dotenv()

app = Flask(__name__, template_folder="templates")

# Configure the app to use SQLAlchemy and SQLite
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///words.db'  # SQLite database file
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Disable warnings

# Initialize the database
db.init_app(app)


    Get API Key


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
    
    # Generate Landing Page
    """
    #return render_template('index.html', test = "testy")
    return render_template('index.html')

@app.route('/generate_sentence', methods=['GET'])
def get_random_sentence():
    """
    Route to generate a random sentence.
    """
    categories = ["noun", "verb", "adjective"]
    sentence = []

    for category in categories:
        word = Word.query.filter_by(category=category).order_by(db.func.random()).first()
        if word:
            sentence.append(word.word)
        else:
            return f"No words found for category: {category}"

    return {"sentence": " ".join(sentence).capitalize() + "."}

@app.route('/words', methods=['GET'])
def get_words():
    """
    Route to fetch all words in the database.
    """
    words = Word.query.all()
    return {"words": [{"word": word.word, "category": word.category} for word in words]}


if __name__ == '__main__':
    # Uncomment the following lines only when you need to create/populate the database.
    # db.create_all()
    # populate_database()
    
    app.run(debug=True)
'''