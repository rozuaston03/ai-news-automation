# Quick Start Guide

Get your automation running in 5 minutes.

## Setup Steps

### 1. Fork and Clone

Fork this repository to your own GitHub account and clone it locally.

### 2. Local Setup

```bash
# Install dependencies
pip install -r requirements.txt

# Create environment file
cp .env.example .env
```

Edit `.env` and add your `GROQ_API_KEY`.

### 3. Run Locally

```bash
export PYTHONPATH=.
python src/main.py
```

### 4. Deploy to GitHub

See [GITHUB_SETUP.md](GITHUB_SETUP.md) for instructions on enabling the 12 PM daily automation.

