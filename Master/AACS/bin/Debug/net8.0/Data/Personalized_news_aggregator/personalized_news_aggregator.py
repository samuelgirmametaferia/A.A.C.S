from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

nltk.download('stopwords')
nltk.download('punkt')

def preprocess_text(text):
  tokens = word_tokenize(text.lower())
  stop_words = set(stopwords.words('english'))
  tokens = [word for word in tokens if word not in stop_words and word.isalnum()]
  return tokens

def build_news_vectorizer(news_articles):
  vectorizer = TfidfVectorizer(tokenizer=preprocess_text)
  article_vectors = vectorizer.fit_transform(news_articles)
  return vectorizer, article_vectors

def get_personalized_news(user_interests, news_articles, vectorizer, article_vectors):
  user_interest_vector = vectorizer.transform(user_interests)
  similarities = cosine_similarity(user_interest_vector, article_vectors)
  sorted_indices = similarities.argsort()[0][::-1]
  return [news_articles[i] for i in sorted_indices]

# Example usage
news_articles = [
  "This is an article about technology.",
  "This is an article about sports.",
  "This is an article about politics.",
  "This is another article about technology."
]

user_interests = "I am interested in technology and sports."

vectorizer, article_vectors = build_news_vectorizer(news_articles)
personalized_news = get_personalized_news(user_interests, news_articles, vectorizer, article_vectors)

print(personalized_news)