from google.cloud import vision

client = vision.ImageAnnotatorClient()

def identify_cloud(image_path):
  with open(image_path, 'rb') as image_file:
    content = image_file.read()
  image = vision.Image(content=content)
  response = client.label_detection(image=image)
  labels = response.label_annotations
  for label in labels:
    print(f'Label: {label.description}, Score: {label.score}')

"

"study_buddy.py"