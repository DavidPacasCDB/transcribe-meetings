from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend import api_asr

app = FastAPI()

# CORS setup for frontend-backend communication
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include the ASR API router for audio transcription under /api
app.include_router(api_asr.router, prefix="/api")

@app.get("/")
def read_root():
    return {"message": "InsightLens backend is running."}
