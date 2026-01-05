import feedparser
import logging
import time
from src.config import Config

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class NewsFetcher:
    def __init__(self, db_logger=None):
        self.feeds = Config.FEEDS
        self.db_logger = db_logger

    def fetch_feed_with_retry(self, url, max_retries=3):
        for attempt in range(max_retries):
            try:
                feed = feedparser.parse(url)
                if feed.bozo:
                    raise Exception(f"Feed error: {feed.bozo_exception}")
                return feed
            except Exception as e:
                wait_time = 2 ** attempt
                logger.warning(f"Attempt {attempt + 1} failed for {url}: {e}. Retrying in {wait_time}s...")
                time.sleep(wait_time)
        return None

    def fetch_latest_news(self, limit_per_feed=Config.LIMIT_PER_FEED):
        all_articles = []
        for url in self.feeds:
            logger.info(f"Fetching from: {url}")
            feed = self.fetch_feed_with_retry(url)
            
            if not feed or not feed.entries:
                logger.warning(f"Skipping {url} after retries or no entries.")
                continue

            count = 0
            for entry in feed.entries:
                if count >= limit_per_feed:
                    break
                
                title = entry.get("title", "No Title")
                
                # Duplicate checking
                if self.db_logger and self.db_logger.is_duplicate(title):
                    logger.info(f"Skipping duplicate: {title}")
                    continue
                
                article = {
                    "title": title,
                    "link": entry.get("link", "#"),
                    "published": entry.get("published", entry.get("updated", "Unknown Date")),
                    "summary": entry.get("summary", ""),
                    "source": feed.feed.get("title", "Unknown Source")
                }
                all_articles.append(article)
                count += 1
        
        return all_articles
