import requests
from decouple import config

# Load the API key from environment variables using decouple
ELEVEN_LABS_API_KEY = config("ELEVEN_LABS_API_KEY")

# Eleven Labs - Convert Text to Speech (Optimized for speed)
def convert_text_to_speech(message):

    # Define Data (Body) - Optimized settings for faster generation
    body = {
        "text": message,
        "voice_settings": {
            "stability": 0.5,  # Balanced for speed and quality
            "similarity_boost": 0.5
        },
        "model_id": "eleven_turbo_v2"  # Use fastest model
    }

    # Define voice - Koro
    voice_Koro = "cwdmeUHVFO9BmZhUar4w"

    # Construct Headers and Endpoint
    headers = {
        "xi-api-key": ELEVEN_LABS_API_KEY, 
        "Content-Type": "application/json", 
        "accept": "audio/mpeg"
    }
    endpoint = f"https://api.elevenlabs.io/v1/text-to-speech/{voice_Koro}"

    # Send request with timeout for faster failure
    try:
        response = requests.post(
            endpoint, 
            json=body, 
            headers=headers,
            timeout=10  # 10 second timeout
        )
        response.raise_for_status()
    except requests.exceptions.Timeout:
        print("Error: Request timed out")
        return None
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None

    # Handle Response
    if response.status_code == 200:
        return response.content
    else:
        print(f"Error: Received status code {response.status_code}")
        return None
