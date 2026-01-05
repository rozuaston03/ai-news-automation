# AI News Automation (Production Ready)

Welcome to the **AI News Automation** project. This system is a fully automated, production-grade pipeline that fetches the latest AI research and news, summarizes it using Groq's Llama 3 state-of-the-art model, and delivers a daily brief via Telegram.

## Features

- **RSS Aggregation**: Monitors top sources like OpenAI, Google DeepMind, TechCrunch, MIT, and The Verge.
- **LLM Summarization**: Uses Groq API (Llama 3.3 70B) for 2-3 bullet-point high-density summaries.
- **Multi-Channel Delivery**: Generates Markdown reports and sends brief updates to Telegram.
- **GitHub Actions Integration**: Runs automatically every day at 12 PM UTC.
- **Robustness**: Professional logging, error handling, and component testing.

## Documentation

- [Quick Start Guide](QUICK_START.md)
- [GitHub Actions Setup](GITHUB_SETUP.md)
- [API Documentation](API_DOCUMENTATION.md)
- [Troubleshooting](TROUBLESHOOTING.md)

## Architecture

```mermaid
graph LR
    A[RSS Feeds] --> B[NewsFetcher]
    B --> C[Summarizer (Groq API)]
    C --> D[ReportGenerator]
    D --> E[Telegram Botany]
    D --> F[Markdown Logs]
    G[GitHub Actions] -- Trigger --> B
```
