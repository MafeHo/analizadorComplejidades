import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
print(f"API Key found: {bool(api_key)}")

if api_key:
    genai.configure(api_key=api_key)
    
    first_model = None
    print("Listing models...")
    for m in genai.list_models():
        if 'generateContent' in m.supported_generation_methods:
            print(m.name)
            if not first_model:
                first_model = m.name
            
    if first_model:
        print(f"Trying first model: {first_model}")
        try:
            model = genai.GenerativeModel(first_model)
            response = model.generate_content("Hello")
            print(f"SUCCESS with {first_model}: {response.text}")
        except Exception as e:
            print(f"FAILED {first_model}: {e}")
