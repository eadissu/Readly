import openai
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class OpenAIClient:
    """
    Handles interactions with the OpenAI API, including audio transcription.
    """

    def __init__(self, api_key):
        if not api_key:
            raise ValueError("API key is required.")
        openai.api_key = api_key

    def transcribe(self, audio_path, transcription_path="transcription.txt"):
        """
        Transcribes the given audio file using OpenAI's Whisper model.

        Args:
            audio_path (str): Path to the audio file.
            transcription_path (str): Path to save the transcription text file.

        Returns:
            str: The transcribed text, or None if failed.
        """
        try:
            with open(audio_path, "rb") as audio_file:
                response = openai.Audio.transcribe(
                    model="whisper-1",
                    file=audio_file
                )

            transcription = response.get("text", "")
            print(f"Transcription: {transcription}")

            with open(transcription_path, "w") as file:
                file.write(transcription)
                print(f"Transcription saved to {transcription_path}")

            return transcription
        except Exception as e:
            print(f"An error occurred during transcription: {e}")
            return None
