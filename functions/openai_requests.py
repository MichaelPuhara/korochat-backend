import openai
from decouple import config

# Import custom functions
from functions.database import get_recent_messages

# Retrieve Environment Variables
openai.organization = config("OPEN_AI_ORG")
openai.api_key = config("OPEN_AI_KEY")

# Function to convert audio to text using OpenAI Whisper
def convert_audio_to_text(audio_file):
    try:
        # Use faster Whisper-1 model
        transcript = openai.Audio.transcribe(
            model="whisper-1", 
            file=audio_file,
            language="en"  # Specify language for faster processing
        )
        message_text = transcript['text']
        return message_text
    except Exception as e:
        print(f"Transcription error: {e}")
        return

# Open AI ChatGPT - Optimized for speed
def get_chat_response(message_input):
    messages = get_recent_messages()
    user_message = {"role": "user", "content": message_input}
    messages.append(user_message)
    print(messages)

    try:
        # Use GPT-3.5-turbo for much faster responses (10x faster than GPT-4)
        # If you need GPT-4, use "gpt-4-turbo" for 2x speed improvement
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # Much faster than gpt-4
            messages=messages,
            temperature=0.7,
            max_tokens=150,  # Limit response length for faster TTS
            stream=False  # Set to True for streaming if needed
        )

        message_text = response["choices"][0]["message"]["content"]
        return message_text
    except Exception as e:
        print(f"Chat completion error: {e}")
        return
