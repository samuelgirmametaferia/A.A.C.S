from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

def load_data(filename):
  data = np.loadtxt(filename, delimiter=",")
  return data

def calculate_similarity(data):
  user_item_matrix = data
  similarity_matrix = cosine_similarity(user_item_matrix)
  return similarity_matrix

def recommend_genres(user_id, similarity_matrix, data, top_n=5):
  user_vector = data[user_id]
  similarities = similarity_matrix[user_id]
  sorted_indices = np.argsort(similarities)[::-1]
  recommended_genres = []
  for i in sorted_indices[1:top_n+1]:
    genre = data[i, -1]
    recommended_genres.append(genre)
  return recommended_genres

if __name__ == "__main__":
  data = load_data("music_data.csv")
  similarity_matrix = calculate_similarity(data)
  user_id = 0  
  recommendations = recommend_genres(user_id, similarity_matrix, data)
  print(f"Recommended genres for user {user_id}: {recommendations}")