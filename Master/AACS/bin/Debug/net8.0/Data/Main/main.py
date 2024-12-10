from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, LSTM
import numpy as np
import pandas as pd

def load_data(filename):
  df = pd.read_csv(filename)
  X = df[['age', 'weight', 'height', 'activity_level']].values
  y = df['target_weight'].values
  return X, y

def build_model():
  model = Sequential()
  model.add(Dense(64, activation='relu', input_shape=(4,)))
  model.add(LSTM(32))
  model.add(Dense(1))
  model.compile(loss='mean_squared_error', optimizer='adam')
  return model

def train_model(X, y, epochs=100):
  model = build_model()
  model.fit(X, y, epochs=epochs)
  return model

def predict_weight(model, age, weight, height, activity_level):
  data = np.array([[age, weight, height, activity_level]])
  prediction = model.predict(data)
  return prediction[0][0]

if __name__ == '__main__':
  X, y = load_data('workout_data.csv')
  model = train_model(X, y)
  
  age = 30
  weight = 70
  height = 175
  activity_level = 2
  predicted_weight = predict_weight(model, age, weight, height, activity_level)
  print(f'Predicted weight: {predicted_weight}')