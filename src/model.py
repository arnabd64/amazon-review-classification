from pydantic import BaseModel, Field


class TextRequest(BaseModel):
    id: str = Field()
    text: str = Field(..., min_length=10, max_length=512)
    
    
class SentimentResponse(TextRequest):
    label: str = Field(...)
    score: float = Field(...)