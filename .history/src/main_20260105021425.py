import logging
import os
from datetime import datetime
from src.config import Config
from src.news_fetcher import NewsFetcher
from src.summarizer import Summarizer
from src.telegram_sender import TelegramSender
from src.report_generator import ReportGenerator
from src.db_logger import DBLogger

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
    
    db_logger = DBLogger()
    fetcher = NewsFetcher(db_logger=db_logger)
    summarizer = Summarizer()
    tg_sender = TelegramSender()
    
    # 1. Fetch
    logger.info("Fetching articles...")
    articles = fetcher.fetch_latest_news()
    if not articles:
        logger.warning("No new articles found today or all were duplicates.")
        db_logger.log_run(0, "success_no_new_content")
        return

    # 2. Summarize & Filter
    final_articles = []
    min_relevance = 6 # Only include articles with score >= 6
    
    for i, article in enumerate(articles):
        logger.info(f"Summarizing ({i+1}/{len(articles)}): {article['title']}")
        summary, score = summarizer.summarize(article['title'], article['summary'] or article['title'])
        
        if score < min_relevance:
            logger.info(f"Filtering out low-relevance article ({score}/10): {article['title']}")
            continue
            
        article['summary'] = summary
        article['relevance'] = score
        final_articles.append(article)
        
        # Log to DB
        db_logger.log_article(article['title'], article['link'], article['source'], article['published'])

    if not final_articles:
        logger.warning("No articles passed the relevance threshold.")
        db_logger.log_run(0, "success_all_filtered")
        return

    # 3. Generate Report
    report_md = ReportGenerator.generate_markdown(final_articles)
    
    # 4. Save to local file
    report_path = f"logs/report_{datetime.now().strftime('%Y%m%d')}.md"
    with open(report_path, "w", encoding="utf-8") as f:
        f.write(report_md)
    logger.info(f"Report saved to {report_path}")

    # 5. Deliver to Telegram
    logger.info("Delivering to Telegram...")
    tg_text = ReportGenerator.generate_telegram_summary(final_articles)
    tg_sender.send_message(tg_text)

    # Log successful run
    db_logger.log_run(len(final_articles), "success")
    logger.info("AI News Automation Cycle Complete.")

if __name__ == "__main__":
    main()
