# Troubleshooting Guide

## Common Issues

### 1. "Workflow not triggering"

- **Cause**: GitHub Actions might be disabled by default on forked repositories.
- **Fix**: Go to **Actions** settings in your repo and enable them. Ensure the cron schedule is correct (`0 12 * * *`).

### 2. "API key invalid"

- **Cause**: Incorrect or expired `GROQ_API_KEY`.
- **Fix**: Test your key with a simple `curl` command or via the [Groq Playground](https://console.groq.com/playground).

### 3. "Telegram not receiving messages"

- **Cause**: Bot not started or incorrect `CHAT_ID`.
- **Fix**: Send a message to your bot first, then visit `https://api.telegram.org/bot<TOKEN>/getUpdates` to find your `chat_id`.

### 4. "No articles found"

- **Cause**: RSS feeds might be down or no new articles were published since the last run.
- **Fix**: Check logs in GitHub Actions to see which feeds failed.

