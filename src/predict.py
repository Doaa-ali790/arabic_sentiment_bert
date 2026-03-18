
from transformers import AutoModelForSequenceClassification, AutoTokenizer
import torch

model_path = "models/sentiment_model"

model = AutoModelForSequenceClassification.from_pretrained(model_path)
tokenizer = AutoTokenizer.from_pretrained("aubmindlab/bert-base-arabertv02")

def predict(text):

    inputs = tokenizer(text, return_tensors="pt")
    outputs = model(**inputs)

    prediction = torch.argmax(outputs.logits)

    return prediction.item()
