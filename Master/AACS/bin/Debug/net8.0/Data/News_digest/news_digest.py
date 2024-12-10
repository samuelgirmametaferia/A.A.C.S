from transformers import pipeline
import requests

summarizer = pipeline("summarization")

def get_news_articles(topic):
  url = f"https://newsapi.org/v2/top-headlines?q={topic}&apiKey=YOUR_NEWS_API_KEY"
  response = requests.get(url)
  data = response.json()
  return data['articles']

def summarize_articles(articles):
  summaries = []
  for article in articles:
    summary = summarizer(article['content'], max_length=100, min_length=30, do_sample=False)[0]['summary_text']
    summaries.append(summary)
  return summaries

if __name__ == "__main__":
  user_topic = input("Enter your preferred news topic: ")
  articles = get_news_articles(user_topic)
  summaries = summarize_articles(articles)
  for summary in summaries:
    print(summary)