import feedparser
import logging
from src.config import Config

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class NewsFetcher:
    def __init__(self):
        self.feeds = Config.FEEDS

    def fetch_latest_news(self, limit_per_feed=Config.LIMIT_PER_FEED):
        all_articles = []
        for url in self.feeds:
            logger.info(f"Fetching from: {url}")
            try:
                feed = feedparser.parse(url)
                if not feed.entries:
                    logger.warning(f"No entries found for {url}")
                    continue

                count = 0
                for entry in feed.entries:
                    if count >= limit_per_feed:
                        break
                    
                    article = {
                        "title": entry.get("title", "No Title"),
                        "link": entry.get("link", "#"),
                        "published": entry.get("published", entry.get("updated", "Unknown Date")),
                        "summary": entry.get("summary", ""),
                        "source": feed.feed.get("title", "Unknown Source")
                    }
                    all_articles.append(article)
                    count += 1
            except Exception as e:
                logger.error(f"Error fetching {url}: {e}")
        
        return all_articles
