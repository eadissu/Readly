# Reference: https://github.com/edenhandom/mood-mix/blob/main/app.py

"""
The main purpose of this file is to run the app. Call the backend functions, including
OpenAI integration (if needed).
"""
from flask import Flask, render_template, request
from gTTS_text_to_speech import generate_speech

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    action = None
    word = "dog"  # Default word

    if request.method == 'POST':
        action = request.form.get('action')

    if action == "listen":
        print("Word: " + word)
        generate_speech(word)  # Call the function to generate and play speech

    return render_template('index.html', content=word)

if __name__ == '__main__':
    app.run(debug=True)
