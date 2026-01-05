import feedparser
import requests
from datetime import datetime

class NewsFetcher:
    def __init__(self):
        self.feeds = [
            "https://openai.com/news/rss.xml",
            "https://deepmind.google/blog/rss.xml",
            "https://techcrunch.com/category/artificial-intelligence/feed/",
            "https://www.theverge.com/ai-artificial-intelligence/rss/index.xml",
            "https://news.mit.edu/rss/topic/artificial-intelligence2"
        ]

    def fetch_latest_news(self, limit_per_feed=2):
        all_articles = []
        for url in self.feeds:
            print(f"Fetching from: {url}")
            try:
                feed = feedparser.parse(url)
                count = 0
                for entry in feed.entries:
                    if count >= limit_per_feed:
                        break
                    
                    article = {
                        "title": entry.get("title", "No Title"),
                        "link": entry.get("link", "#"),
                        "published": entry.get("published", "Unknown Date"),
                        "summary": entry.get("summary", ""),
                        "source": feed.feed.get("title", "Unknown Source")
                    }
                    all_articles.append(article)
                    count += 1
            except Exception as e:
                print(f"Error fetching {url}: {e}")
        
        return all_articles

if __name__ == "__main__":
    fetcher = NewsFetcher()
    news = fetcher.fetch_latest_news(limit_per_feed=1)
    for n in news:
        print(f"--- {n['title']} ---")
        print(f"Source: {n['source']}")
        print(f"Link: {n['link']}")
