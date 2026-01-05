import pytest
from src.report_generator import ReportGenerator
from src.telegram_sender import TelegramSender

def test_report_generator_markdown():
    articles = [{
        "title": "A", "source": "S", "published": "D", "summary": "Sum", "link": "L"
    }]
    report = ReportGenerator.generate_markdown(articles)
    assert "# AI Daily News Report" in report
    assert "## A" in report

def test_telegram_sender_config_missing(mocker):
    mocker.patch('src.config.Config.TELEGRAM_BOT_TOKEN', None)
    sender = TelegramSender()
    assert sender.send_message("test") is False

def test_telegram_sender_success(mocker):
    mocker.patch('src.config.Config.TELEGRAM_BOT_TOKEN', "token")
    mocker.patch('src.config.Config.TELEGRAM_CHAT_ID', "123")
    mock_post = mocker.patch('requests.post')
    mock_post.return_value.status_code = 200
    
    sender = TelegramSender()
    assert sender.send_message("test") is True
