# API Documentation

This project integrates with two primary APIs.

## Integration Details

### 1. Groq API

- **Endpoint**: `https://api.groq.com/openai/v1/chat/completions` (via Python client)
- **Model**: `llama-3.3-70b-versatile`
- **Purpose**: High-speed summarization of news articles.
- **Consumption**: ~10-15 articles per day.

### 2. Telegram Bot API

- **Endpoint**: `https://api.telegram.org/bot<TOKEN>/sendMessage`
- **Purpose**: Delivery of daily news briefs.
- **Format**: MarkdownV2/Markdown.
- **BotFather**: Use @BotFather to create your bot and get the token.

### 3. RSS Feeds

We pull from the following sources daily:

- OpenAI News
- Google DeepMind Blog
- TechCrunch (AI category)
- The Verge (AI section)
- MIT News (AI topic)

