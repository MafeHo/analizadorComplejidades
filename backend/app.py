from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import sys
import os

# Add current directory to sys.path to ensure we can import src
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from src.main import analyze_algorithm

app = FastAPI()

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins for development
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class AnalysisRequest(BaseModel):
    code: str
    translate: bool = False

@app.post("/analyze")
async def analyze(request: AnalysisRequest):
    try:
        # analyze_algorithm expects a filepath, but we have the code in memory.
        # We can write to a temp file or modify analyze_algorithm to accept string.
        # Modifying analyze_algorithm is better, but for now to minimize changes,
        # I'll write to a temp file as the original code did.
        
        temp_filename = "temp_api_input.txt"
        with open(temp_filename, "w", encoding="utf-8") as f:
            f.write(request.code)
            
        # Call the analysis function
        result = analyze_algorithm(temp_filename, translate_mode=request.translate)
        
        print("DEBUG RESPONSE:", result) # Add this line
        
        # Clean up temp file (optional, maybe keep for debugging)
        # os.remove(temp_filename)
        
        return result
    except Exception as e:
        import traceback
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/")
def read_root():
    return {"message": "Algorithm Complexity Analyzer API is running"}
