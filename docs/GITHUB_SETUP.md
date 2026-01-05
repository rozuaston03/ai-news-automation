# GitHub Setup Guide

To enable the daily automation (12 PM UTC), you must configure your GitHub Secrets.

## Configuration Steps

### 1. Go to Repository Settings

Navigate to your repository on GitHub and click on **Settings** -> **Secrets and variables** -> **Actions**.

### 2. Add Repository Secrets

Add the following secrets:

- `GROQ_API_KEY`: Your API key from [Groq Console](https://console.groq.com/).
- `TELEGRAM_BOT_TOKEN`: The token from your Telegram Bot (via @BotFather).
- `TELEGRAM_CHAT_ID`: Your chat ID or the channel ID where news should be sent.

### 3. Enable Actions

Go to the **Actions** tab of your repository and click "I understand my workflows, go ahead and enable them."

### 4. Verify

You can manually trigger the workflow by clicking "Daily AI News Automation" -> "Run workflow".

