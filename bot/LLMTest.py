import random
from groq import Groq
import bot.bot_core as bot_core

from dotenv import load_dotenv
import os
load_dotenv()


def generate_comment_with_groq(title, content):
    client = Groq(api_key=os.getenv("GROQ_API_KEY"))
    prompt = (
        f"Read the following Reddit post and write a meaningful, relevant, and upvote-worthy comment:\n\n"
        f"Title: {title}\nContent: {content}\n\nComment:"
    )
    completion = client.chat.completions.create(
        model="compound-beta",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=1,
        max_completion_tokens=1024,
        top_p=1,
        stream=True,
        stop=None,
    )

    comment = ""
    for chunk in completion:
        comment += chunk.choices[0].delta.content or ""
    return comment

bot = bot_core.RedditBot(dry_run=True)
post = bot.fetch_random_post("AskReddit")
title = post.title
content = post.selftext
comment = generate_comment_with_groq(title, content)

print("Title:", title)
print("Content:", content)
print("Generated comment:", comment)