# InsightLens: AI-Powered Multimodal Meeting Intelligence Platform

## Overview
InsightLens transforms business meetings into actionable, searchable knowledge. It ingests meeting recordings, slides, and chat logs, then uses advanced AI to:
- Transcribe and summarize discussions
- Extract and classify action items, decisions, and key topics
- Auto-generate visual meeting minutes
- Enable semantic search across all past meetings
- Translate and localize meeting content
- Detect and flag compliance or sensitive topics

## Key Hugging Face Tasks Used
- Automatic Speech Recognition (ASR)
- Summarization
- Text Classification
- Translation
- Question Answering
- (Optional) Image-to-Text, Visual Document Retrieval

## Tech Stack
- **Frontend:** Next.js (React), Tailwind CSS
- **Backend:** FastAPI (Python), Celery, PostgreSQL, Elasticsearch
- **AI Integration:** Hugging Face Transformers
- **Cloud:** AWS/GCP/Azure
- **APIs:** Zoom/Teams/Google Meet, Slack/Teams

## Architecture
```
[User] <-> [Next.js Frontend] <-> [FastAPI Backend] <-> [AI Services, DB, Search]
```

## Getting Started
- `frontend/` - Next.js app
- `backend/` - FastAPI app
- `ai_models/` - Hugging Face model integration
- `data_ingestion/` - Meeting data ingestion scripts

---
This project is designed for scalability, real-world value, and portfolio impact.
