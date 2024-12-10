from datetime import datetime
import tensorflow as tf
from transformers import pipeline

model_name = "gpt2"
generator = pipeline("text-generation", model=model_name)

def generate_prompt(theme):
  prompt = f"Write a short story about {theme}."
  return generator(prompt, max_length=100, num_return_sequences=3)[0]["generated_text"]

def log_dream(dream_text):
  timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
  with open("dream_journal.txt", "a") as f:
    f.write(f"{timestamp}: {dream_text}\n")

while True:
  theme = input("Enter a dream theme: ")
  prompt = generate_prompt(theme)
  print("AI-generated story prompt:")
  print(prompt)
  dream_text = input("Enter your dream: ")
  log_dream(dream_text)
  print("Dream logged successfully!")