import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;
import java.util.List;

public class NewsAggregator {

  public static void main(String[] args) {
    List<NewsArticle> articles = new ArrayList<>();
    // ... populate articles list with news articles

    // Get user preferences
    String[] preferredTopics = {"technology", "science"};

    // Filter and rank articles based on preferences
    List<NewsArticle> filteredArticles = filterArticles(articles, preferredTopics);
    Collections.sort(filteredArticles, Comparator.comparingInt(NewsArticle::getRelevance));

    // Display top ranked articles
    for (NewsArticle article : filteredArticles) {
      System.out.println(article.getTitle());
    }
  }

  static List<NewsArticle> filterArticles(List<NewsArticle> articles, String[] preferredTopics) {
    List<NewsArticle> filteredArticles = new ArrayList<>();
    for (NewsArticle article : articles) {
      for (String topic : preferredTopics) {
        if (article.getTopics().contains(topic)) {
          filteredArticles.add(article);
          break;
        }
      }
    }
    return filteredArticles;
  }

  static class NewsArticle {
    private String title;
    private List<String> topics;
    private int relevance;

    // ... getters and setters

    public int getRelevance() {
      return relevance;
    }
  }
}