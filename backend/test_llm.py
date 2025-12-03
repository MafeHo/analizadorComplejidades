import sys
import os
from dotenv import load_dotenv
from google import genai

# Load env
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
print(f"API Key found: {bool(api_key)}")

if api_key:
    try:
        client = genai.Client(api_key=api_key)
        print("Listing models...")
        for m in client.models.list():
            print(m.name)
            
        models_to_try = ['models/gemini-1.5-flash', 'models/gemini-1.5-flash-001', 'models/gemini-1.5-pro', 'models/gemini-pro']
        
        for model_name in models_to_try:
            print(f"Trying {model_name}...")
            try:
                response = client.models.generate_content(
                    model=model_name,
                    contents='Hello',
                )
                print(f"SUCCESS with {model_name}: {response.text}")
                break
            except Exception as e:
                print(f"FAILED {model_name}: {e}")
        print("Response received:")
        print(response.text)
    except Exception as e:
        print(f"Error: {e}")
else:
    print("No API Key found")
