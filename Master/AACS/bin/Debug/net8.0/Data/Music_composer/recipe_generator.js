const express = require('express');
const mongoose = require('mongoose');

const app = express();
mongoose.connect('mongodb://localhost:27017/recipes', { useNewUrlParser: true, useUnifiedTopology: true });

const RecipeSchema = new mongoose.Schema({
  name: String,
  ingredients: Array,
  instructions: String,
  dietaryRestrictions: Array
});

const Recipe = mongoose.model('Recipe', RecipeSchema);

app.get('/recipes', async (req, res) => {
  const { restrictions, ingredients } = req.query;
  const query = {};
  if (restrictions) {
    query.dietaryRestrictions = { $in: restrictions.split(',') };
  }
  if (ingredients) {
    query.ingredients = { $all: ingredients.split(',') };
  }
  const recipes = await Recipe.find(query);
  res.json(recipes);
});

app.listen(3000, () => console.log('Server running on port 3000'));