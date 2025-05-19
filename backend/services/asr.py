from transformers import pipeline
from tempfile import NamedTemporaryFile
import torch

# Load the ASR pipeline once at module level for efficiency
asr_pipeline = pipeline("automatic-speech-recognition", model="openai/whisper-base", device=0 if torch.cuda.is_available() else -1)

def transcribe_audio(audio_bytes: bytes) -> str:
    with NamedTemporaryFile(suffix=".wav") as temp_audio:
        temp_audio.write(audio_bytes)
        temp_audio.flush()
        result = asr_pipeline(temp_audio.name)
        return result["text"]
