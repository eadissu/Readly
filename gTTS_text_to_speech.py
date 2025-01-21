from gtts import gTTS
import os

def generate_speech(word, file_path="word_audio.mp3", play_audio=True):
    """
    Converts a given word to speech and saves it as an MP3 file.

    Args:
        word (str): The word to convert to speech.
        file_path (str): The file path to save the MP3 file.
        play_audio (bool): Whether to play the audio file after saving.

    Returns:
        str: The path to the saved MP3 file, or None if failed.
    """
    try:
        tts = gTTS(text=word, lang='en')
        tts.save(file_path)
        print(f"Audio file saved as {file_path}")

        if play_audio:
            os.system(f"afplay {file_path}")  # For macOS
            # os.system(f"start {file_path}")  # For Windows
            # os.system(f"mpg321 {file_path}")  # For Linux

        return file_path
    except Exception as e:
        print(f"An error occurred during text-to-speech: {e}")
        return None
