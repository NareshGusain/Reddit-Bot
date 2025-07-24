# 🤖 Reddit Comment Bot

[![Python](https://img.shields.io/badge/Python-3.7%2B-blue.svg)](https://www.python.org/downloads/)
[![PRAW](https://img.shields.io/badge/PRAW-7.8.1-orange.svg)](https://praw.readthedocs.io/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

An intelligent Reddit commenting bot designed to help grow your karma responsibly. Features smart post filtering, rate limiting, and comprehensive safety measures to ensure compliance with Reddit's terms of service.

## 🚀 Quick Start

### Prerequisites

- Python 3.7 or higher
- A Reddit account
- Reddit API credentials (free)

### 1. Clone the Repository

```bash
git clone https://github.com/NareshGusain/Reddit-Bot.git
cd RedBot
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Get Reddit API Credentials

1. Go to [Reddit Apps](https://www.reddit.com/prefs/apps)
2. Login and create a new app (type: "script")
3. Copy your client ID and secret

### 4. Configure the Bot

Create a `.env` file with your credentials:

```env
REDDIT_CLIENT_ID=your_client_id
REDDIT_CLIENT_SECRET=your_client_secret
REDDIT_USER_AGENT=RedditBot/1.0 by YourUsername
REDDIT_USERNAME=your_reddit_username
REDDIT_PASSWORD=your_reddit_password
MAX_COMMENTS_PER_SUBREDDIT=5
```

### 5. Run the Bot

**Safe testing (recommended first):**
```bash
python reddit_bot.py --dry-run --max-comments 2
python reddit_bot.py --interactive
```

**Live operation:**
```bash
python reddit_bot.py --max-comments 3
python reddit_bot.py
```

## 📖 Usage Guide

### Command Line Options

```bash
python reddit_bot.py [OPTIONS]

Options:
  --dry-run              Test without posting comments
  --interactive          Run in interactive mode
  --max-comments N       Limit total comments to N
  --help                 Show help message
```

### Configuration Files

#### `config.py` - Main Configuration

```python
TARGET_SUBREDDITS = [
    'AskReddit',
    'funny',
    'todayilearned',
    # Add your preferred subreddits
]

COMMENT_TEMPLATES = [
    "Great post! Thanks for sharing.",
    "This is really interesting!",
    # Add more comments here
]

COMMENT_BEHAVIOR = {
    'max_retries': 3,
    'avoid_own_posts': True,
    'avoid_already_commented': True,
}

RATE_LIMITS = {
    'min_delay': 30,
    'max_delay': 120,
}
```

## 🛡️ Safety Features

- Rate limiting between comments
- Post age and score filtering
- Duplicate and own post avoidance
- Dry-run and interactive modes
- Comprehensive logging to `bot.log`

## 🔧 Customization

- Add subreddits in `config.py`
- Edit comment templates in `config.py` (or `comments.txt` if you use it)
- Adjust rate limits and behavior in `config.py`

## 📄 License

MIT License - see the [LICENSE](LICENSE) file for details.

---

**Note:**  
- If you removed `comments.txt`, `utils.py`, or `test_credentials.py`, remove references to them in the README.
- If you changed the main bot logic to `bot_core.py`, mention that `reddit_bot.py` is the entry point and imports the bot from `bot_core.py`.
- Remove instructions for any setup scripts you deleted.

---
