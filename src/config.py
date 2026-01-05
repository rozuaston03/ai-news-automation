import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    # API Keys
    GROQ_API_KEY = os.getenv("GROQ_API_KEY")
    TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
    TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

    # Model Settings
    GROQ_MODEL = "llama-3.3-70b-versatile"
    TEMPERATURE = 0.5
    MAX_TOKENS = 256

    # News Settings
    LIMIT_PER_FEED = 3
    FEEDS = [
        "https://openai.com/news/rss.xml",
        "https://deepmind.google/blog/rss.xml",
        "https://techcrunch.com/category/artificial-intelligence/feed/",
        "https://www.theverge.com/ai-artificial-intelligence/rss/index.xml",
        "https://news.mit.edu/rss/topic/artificial-intelligence2"
    ]

    @classmethod
    def validate(cls):
        if not cls.GROQ_API_KEY:
            print("WARNING: GROQ_API_KEY not found.")
        if not cls.TELEGRAM_BOT_TOKEN:
            print("WARNING: TELEGRAM_BOT_TOKEN not found.")
        if not cls.TELEGRAM_CHAT_ID:
            print("WARNING: TELEGRAM_CHAT_ID not found.")
