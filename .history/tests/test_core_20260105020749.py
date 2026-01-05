import pytest
from src.config import Config
from src.news_fetcher import NewsFetcher

def test_config_defaults():
    assert Config.GROQ_MODEL == "llama-3.3-70b-versatile"
    assert len(Config.FEEDS) > 0

def test_news_fetcher_init():
    fetcher = NewsFetcher()
    assert len(fetcher.feeds) == len(Config.FEEDS)

def test_news_fetcher_parsing(mocker):
    # Mock feedparser.parse
    mock_feed = mocker.Mock()
    mock_feed.entries = [
        {"title": "Test Title", "link": "https://test.com", "published": "today", "summary": "test summary"}
    ]
    mock_feed.feed = {"title": "Test Source"}
    mocker.patch('feedparser.parse', return_value=mock_feed)
    
    fetcher = NewsFetcher()
    articles = fetcher.fetch_latest_news(limit_per_feed=1)
    
    assert len(articles) == 5
    assert articles[0]['title'] == "Test Title"
    assert articles[0]['source'] == "Test Source"
