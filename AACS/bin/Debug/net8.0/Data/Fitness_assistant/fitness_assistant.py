from tensorflow.keras.models import load_model
import numpy as np

model = load_model('fitness_model.h5')

def predict_exercise(user_input):
  input_data = np.array([user_input])
  prediction = model.predict(input_data)
  exercise = np.argmax(prediction)
  return exercise

while True:
  user_input = input("What exercise are you looking for? ")
  exercise = predict_exercise(user_input)
  print(f"Recommended exercise: {exercise}")