from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from backend.schemas import TranslateRequest, TranslateResponse
from backend.model import Translator

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)