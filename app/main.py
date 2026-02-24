from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from emotion_detector import EmotionDetector
from tts_engine import EmpathyVoiceEngine

import os
import uuid

app = FastAPI()

# Ensure static folder exists
if not os.path.exists("static"):
    os.makedirs("static")

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

detector = EmotionDetector()



@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "emotion": None,
            "intensity": None,
            "audio_file": None
        }
    )


@app.post("/generate", response_class=HTMLResponse)
def generate(request: Request, text: str = Form(...)):

    emotion, intensity = detector.detect_emotion(text)

    tts = EmpathyVoiceEngine()
    audio_path = tts.save_audio(text, emotion, intensity)

    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "emotion": emotion,
            "intensity": round(intensity, 2),
            "audio_file": "/" + audio_path + f"?v={uuid.uuid4().hex}"
        }
    )