from tensorflow.keras.models import load_model
import numpy as np
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer

model = load_model('chatbot_model.h5')
vectorizer = TfidfVectorizer()

stop_words = set(stopwords.words('english'))

def preprocess_text(text):
  tokens = word_tokenize(text.lower())
  tokens = [token for token in tokens if token not in stop_words and token.isalnum()]
  return tokens

def generate_response(user_input):
  processed_input = preprocess_text(user_input)
  input_vector = vectorizer.transform([user_input])
  prediction = model.predict(input_vector)[0]
  response = ""
  for i in range(len(prediction)):
    if prediction[i] > 0.5:
      response += vocabulary[i] + " "
  return response.strip()

vocabulary = []
with open('vocabulary.txt', 'r') as f:
  vocabulary = f.read().splitlines()

while True:
  user_input = input("You: ")
  response = generate_response(user_input)
  print("Chatbot:", response)