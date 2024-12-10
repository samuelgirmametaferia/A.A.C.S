from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

nltk.download('stopwords')
nltk.download('punkt')

def preprocess_text(text):
  tokens = word_tokenize(text)
  stop_words = set(stopwords.words('english'))
  filtered_tokens = [word for word in tokens if word.lower() not in stop_words and word.isalnum()]
  return filtered_tokens

def generate_recipe(ingredients):
  # Implement your recipe generation logic here
  # You can use NLP techniques like keyword extraction, similarity matching,
  # or machine learning models to generate recipes based on the provided ingredients.

  # Example placeholder:
  print("Here's a recipe suggestion based on your ingredients:")
  print("-" * 20)
  print("Recipe Name: Simple Dish")
  print("Ingredients:")
  for ingredient in ingredients:
    print(f"- {ingredient}")
  print("Instructions:")
  print("1. Combine all ingredients in a bowl.")
  print("2. Mix well.")
  print("3. Enjoy!")

# Example usage:
user_ingredients = input("Enter your available ingredients separated by commas: ").split(",")
processed_ingredients = [preprocess_text(ingredient.strip()) for ingredient in user_ingredients]