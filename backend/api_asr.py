from fastapi import APIRouter, UploadFile, File, HTTPException
from backend.services.asr import transcribe_audio

router = APIRouter()

@router.post("/transcribe/")
async def transcribe(file: UploadFile = File(...)):
    if not file.content_type.startswith("audio/"):
        raise HTTPException(status_code=400, detail="Invalid file type. Please upload an audio file.")
    audio_bytes = await file.read()
    transcript = transcribe_audio(audio_bytes)
    return {"transcript": transcript}
