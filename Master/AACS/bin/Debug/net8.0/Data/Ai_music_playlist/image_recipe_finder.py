import cv2
import tensorflow as tf

model = tf.keras.models.load_model('recipe_model.h5')

def find_recipe(image_path):
  image = cv2.imread(image_path)
  image = cv2.resize(image, (224, 224))
  image = image / 255.0
  prediction = model.predict(np.expand_dims(image, axis=0))
  predicted_class = np.argmax(prediction)
  return predicted_class

# Example usage
image_path = 'path/to/your/image.jpg'
recipe_class = find_recipe(image_path)
print(recipe_class)