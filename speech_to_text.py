import openai
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Set your OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

def transcribe_audio(file_path, output_text_file):
    """
    Transcribes the given audio file using OpenAI's Whisper model and saves the result.

    Args:
        file_path (str): Path to the audio file.
        output_text_file (str): Path to save the transcribed text.

    Returns:
        str: The transcribed text.
    """
    try:
        # Open the MP3 file and send it to OpenAI for transcription
        with open(file_path, "rb") as audio_file:
            response = openai.Audio.transcribe(
                model="whisper-1",  # Whisper model
                file=audio_file
            )

        # Extract the transcribed text
        transcribed_text = response.get("text", "")
        print("Transcribed text:", transcribed_text)

        # Save the transcribed text to a file
        with open(output_text_file, "w") as text_file:
            text_file.write(transcribed_text)
            print(f"Transcription saved to {output_text_file}")

        return transcribed_text

    except Exception as e:
        print(f"An error occurred: {e}")
        return None

if __name__ == "__main__":
    # Test the transcription function
    audio_path = "final_output.mp3"  # Ensure this file exists
    text_output_path = "transcription.txt"
    transcribe_audio(audio_path, text_output_path)
