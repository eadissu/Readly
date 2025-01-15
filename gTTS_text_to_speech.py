from gtts import gTTS
import os

# Define the sentence globally
SENTENCE = "The cat sat on the mat."

def generate_speech(file_path="final_test2_output.mp3", play_audio=True):
    """
    Converts the predefined sentence to speech and saves it as an MP3 file.

    Args:
        file_path (str): The file path to save the MP3 file.
        play_audio (bool): Whether to play the audio file after saving.

    Returns:
        str: The path to the saved MP3 file, or None if failed.
    """
    try:
        tts = gTTS(text=SENTENCE, lang='en')
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
