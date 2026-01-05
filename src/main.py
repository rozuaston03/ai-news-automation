import logging
import os
from datetime import datetime
from src.config import Config
from src.news_fetcher import NewsFetcher
from src.summarizer import Summarizer
from src.telegram_sender import TelegramSender
from src.report_generator import ReportGenerator

# Setup logging
os.makedirs("logs", exist_ok=True)
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(f"logs/automation_{datetime.now().strftime('%Y%m%d')}.log"),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

def main():
    logger.info("Initializing AI News Automation Service...")
    Config.validate()
    
    fetcher = NewsFetcher()
    summarizer = Summarizer()
    tg_sender = TelegramSender()
    
    # 1. Fetch
    logger.info("Fetching articles...")
    articles = fetcher.fetch_latest_news()
    if not articles:
        logger.warning("No articles found today.")
        return

    # 2. Summarize
    summarized_articles = []
    for i, article in enumerate(articles):
        logger.info(f"Summarizing ({i+1}/{len(articles)}): {article['title']}")
        summary = summarizer.summarize(article['title'], article['summary'] or article['title'])
        article['summary'] = summary
        summarized_articles.append(article)

    # 3. Generate Report
    report_md = ReportGenerator.generate_markdown(summarized_articles)
    
    # 4. Save to local file
    report_path = f"logs/report_{datetime.now().strftime('%Y%m%d')}.md"
    with open(report_path, "w", encoding="utf-8") as f:
        f.write(report_md)
    logger.info(f"Report saved to {report_path}")

    # 5. Deliver to Telegram
    logger.info("Delivering to Telegram...")
    tg_text = ReportGenerator.generate_telegram_summary(summarized_articles)
    tg_sender.send_message(tg_text)

    logger.info("AI News Automation Cycle Complete.")

if __name__ == "__main__":
    main()
