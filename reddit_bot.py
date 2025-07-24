#!/usr/bin/env python3
"""
Reddit Bot - Automated Comment Bot
A responsible Reddit bot that can post comments across multiple communities.

Usage:
    python reddit_bot.py [options]

Options:
    --dry-run       Test the bot without actually posting comments
    --interactive   Run in interactive mode for manual control
    --help         Show this help message
"""

import praw
import random
import time
import logging
import os
import sys
import argparse
from datetime import datetime, timedelta
from dotenv import load_dotenv
from typing import List, Dict, Optional
import json
import reddit_bot

# Import configuration
from config import (
    TARGET_SUBREDDITS, COMMENT_TEMPLATES, POST_SELECTION, 
    COMMENT_BEHAVIOR, RATE_LIMITS, LOGGING
)


def main():
    parser = argparse.ArgumentParser(description='Reddit Comment Bot')
    parser.add_argument('--dry-run', action='store_true', help='Test the bot without posting comments')
    parser.add_argument('--interactive', action='store_true', help='Run in interactive mode')
    parser.add_argument('--max-comments', type=int, help='Maximum number of comments to post')
    args = parser.parse_args()

    if not os.path.exists('.env'):
        print("❌ .env file not found!")
        sys.exit(1)

    bot = reddit_bot.RedditBot(dry_run=args.dry_run)
    try:
        if args.interactive:
            bot.interactive_mode()
        else:
            bot.run_bot(max_comments=args.max_comments)
    except KeyboardInterrupt:
        print("\n👋 Bot stopped by user")
        bot.save_commented_posts()
    except Exception as e:
        bot.logger.error(f"💥 Unexpected error: {e}")
        bot.save_commented_posts()

if __name__ == "__main__":
    main()
