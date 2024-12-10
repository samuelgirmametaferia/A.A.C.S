import tensorflow as tf
import numpy as np
from tensorflow.keras.models import load_model

# Load the pre-trained music composition model
model = load_model('music_composition_model.h5')

# Define the input and output dimensions
input_dim = 128
output_dim = 64

# Generate a sequence of notes
notes = np.random.randint(0, output_dim, size=input_dim)

# Predict the next note
prediction = model.predict(notes.reshape(1, input_dim))

# Convert the prediction to a note
next_note = np.argmax(prediction)

# Print the predicted note
print(next_note)



"InteractiveStorybook.py"