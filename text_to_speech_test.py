from gtts import gTTS
import os

# Define the sentence you want to convert to speech
sentence = "The dog sat on the mat."

# Convert text to speech and save as an MP3 file
file_path = "final_output.mp3"
tts = gTTS(text=sentence, lang='en')
tts.save(file_path)

print(f"Audio file saved as {file_path}")

# Play the audio file (requires a player)
# os.system(f"start {file_path}")  # For Windows
os.system(f"afplay {file_path}")  # For macOS
# os.system(f"mpg321 {file_path}")  # For Linux