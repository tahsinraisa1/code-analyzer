from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

# Load the ML model and tokenizer
MODEL_NAME = "cincin2399/codet5-fine-tuned"
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME, token='')
model = AutoModelForSequenceClassification.from_pretrained(MODEL_NAME, token='')

SEVERITY_MAPPING = {0: "Info", 1: "Warning", 2: "Error"}

def perform_ml_analysis(code: str) -> list:
    """
    Use the fine-tuned ML model to analyze the code snippet.
    """
    tokens = tokenizer(code, return_tensors="pt", padding=True, truncation=True)
    outputs = model(**tokens)
    predictions = torch.argmax(outputs.logits, dim=1).tolist()
    print(predictions)

    # Generate results with severity levels
    return [
        {
            "line": 0,  # Placeholder as ML models typically can't pinpoint exact lines
            "message": "Consider optimizing this section.",
            "type": SEVERITY_MAPPING[pred],
        }
        for pred in predictions
    ]
