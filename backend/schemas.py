from pydantic import BaseModel, Field

class TranslateRequest(BaseModel):
    text: str = Field(..., min_length=1, max_length=512)

class TranslateResponse(BaseModel):
    translation: str