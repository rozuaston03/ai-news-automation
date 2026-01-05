import sqlite3
import logging
from datetime import datetime
from src.config import Config

logger = logging.getLogger(__name__)

class DBLogger:
    def __init__(self, db_path="logs/news_automation.db"):
        self.db_path = db_path
        self._init_db()

    def _init_db(self):
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            
            # Table for automation runs
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS runs (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                    article_count INTEGER,
                    status TEXT
                )
            ''')
            
            # Table for summarized articles (for duplicate detection)
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS articles (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    title TEXT UNIQUE,
                    link TEXT,
                    source TEXT,
                    published_at TEXT,
                    summarized_at DATETIME DEFAULT CURRENT_TIMESTAMP
                )
            ''')
            
            conn.commit()
            conn.close()
        except Exception as e:
            logger.error(f"Database initialization error: {e}")

    def log_run(self, article_count, status="success"):
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            cursor.execute('INSERT INTO runs (article_count, status) VALUES (?, ?)', (article_count, status))
            conn.commit()
            conn.close()
        except Exception as e:
            logger.error(f"Error logging run: {e}")

    def log_article(self, title, link, source, published_at):
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            cursor.execute('''
                INSERT OR IGNORE INTO articles (title, link, source, published_at) 
                VALUES (?, ?, ?, ?)
            ''', (title, link, source, published_at))
            conn.commit()
            conn.close()
        except Exception as e:
            logger.error(f"Error logging article: {e}")

    def is_duplicate(self, title):
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            cursor.execute('SELECT 1 FROM articles WHERE title = ?', (title,))
            exists = cursor.fetchone() is not None
            conn.close()
            return exists
        except Exception as e:
            logger.error(f"Error checking duplicate: {e}")
            return False
