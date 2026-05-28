# 🤖 Reddit Post Fetcher

A Python CLI tool that fetches top 5 posts
from any subreddit directly in your terminal.

## ✨ Features
- Fetch top posts from any subreddit
- Shows upvotes, comments and link
- Error handling for invalid subreddits
- No API key needed!

## 🚀 Usage
\```bash
python reddit-post-fetcher.py funny
python reddit-post-fetcher.py python
python reddit-post-fetcher.py india
\```

## 📤 Output
\```
----------------------------------------------------------------
1. Post title here
👍 Likes : 6524  | 💬 Comments : 72
🔗 link : https://...
----------------------------------------------------------------
\```

## 🛠️ Tech Stack
![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)

## 📁 Project Structure
\```
├── reddit-post-fetcher.py
└── README.md
\```

## 🔑 API Used
Reddit Public JSON API — no key needed!
https://www.reddit.com/r/{subreddit}/top.json