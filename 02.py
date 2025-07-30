from transformers import GPT2Tokenizer
from datasets import load_dataset, Dataset
import torch

# Load tokenizer
tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
tokenizer.pad_token = tokenizer.eos_token

# Read your preprocessed text
with open("mental_health_chat_data.txt", "r", encoding="utf-8") as f:
    lines = f.read().split("\n\n")

# Create dataset from lines
dataset = Dataset.from_dict({"text": lines})

# Tokenize the dataset
def tokenize(example):
    return tokenizer(example["text"], truncation=True, padding="max_length", max_length=128)

tokenized_dataset = dataset.map(tokenize, batched=True)
