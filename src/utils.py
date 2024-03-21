from transformers import pipeline
from src.model import TextRequest, SentimentResponse


def download_model():
    return pipeline("text-classification", "arnabdhar/distilbert-base-amazon-multi")


sentiment = download_model()


def classify(request: TextRequest):
    output = sentiment(request.text)
    return SentimentResponse(**request.model_dump(), **output[0])


if __name__ == "__main__":
    _ = download_model()