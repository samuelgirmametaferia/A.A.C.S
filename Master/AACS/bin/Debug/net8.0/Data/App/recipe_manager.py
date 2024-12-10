class RecipeManager:
  def __init__(self):
    self.recipes = {
      'recipe1': {'ingredients': ['chicken', 'broccoli', 'rice'], 'instructions': 'Cook chicken, steam broccoli, cook rice.'},
      'recipe2': {'ingredients': ['pasta', 'tomato sauce', 'ground beef'], 'instructions': 'Cook pasta, brown ground beef, mix with sauce.'},
      'recipe3': {'ingredients': ['eggs', 'bread', 'cheese'], 'instructions': 'Fry eggs, toast bread, melt cheese.'}
    }

  def find_recipes(self, ingredients):
    matching_recipes = []
    for recipe_name, recipe_data in self.recipes.items():
      if all(ingredient in recipe_data['ingredients'] for ingredient in ingredients):
        matching_recipes.append(recipe_data)
    return matching_recipes