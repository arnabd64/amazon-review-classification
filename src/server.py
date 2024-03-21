from fastapi import FastAPI, Depends
from fastapi.responses import PlainTextResponse
from src.utils import download_model, classify
from src.model import SentimentResponse
from typing import Annotated


app = FastAPI(on_startup=[download_model])


@app.get("/", response_class=PlainTextResponse)
async def root():
    return "server is running"


@app.post("/classify", response_model=SentimentResponse)
async def classify(response: Annotated[SentimentResponse, Depends(classify)]):
    return response