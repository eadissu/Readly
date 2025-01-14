import openai

# Set your OpenAI API key
openai.api_key = "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"

# Path to the MP3 file
audio_file_path = "final_output.mp3"

# Open the MP3 file and send it to OpenAI for transcription
try:
    with open(audio_file_path, "rb") as audio_file:
        response = openai.Audio.transcribe(
            model="whisper-1",  # Whisper model
            file=audio_file
        )

    # Extract the transcribed text
    transcribed_text = response.get("text", "")
    print("Transcribed text:", transcribed_text)

    # Save the transcribed text to a file
    with open("transcription.txt", "w") as text_file:
        text_file.write(transcribed_text)
        print("Transcription saved to transcription.txt")

except Exception as e:
    print(f"An error occurred: {e}")
