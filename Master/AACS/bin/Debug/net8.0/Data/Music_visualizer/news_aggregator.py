import scrapy
import nltk

class NewsAggregatorSpider(scrapy.Spider):
  name = "news_aggregator"
  start_urls = ["https://www.example.com/news", "https://www.another_news_site.com/"]

  def parse(self, response):
    for article in response.css("article"):
      title = article.css("h2::text").get()
      link = article.css("a::attr(href)").get()
      
      yield {
        "title": title,
        "link": link
      }

nltk.download("punkt")
nltk.download("stopwords")

# ... (Code to process and personalize news articles) ...