from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.mobilenet_v2 import MobileNetV2, preprocess_input
import numpy as np

model = MobileNetV2(weights='imagenet')

def identify_plant(image_path):
  img = image.load_img(image_path, target_size=(224, 224))
  x = image.img_to_array(img)
  x = np.expand_dims(x, axis=0)
  x = preprocess_input(x)
  preds = model.predict(x)
  decoded_preds = decode_predictions(preds, top=3)[0]
  return decoded_preds

"plant_identifier_app.py"