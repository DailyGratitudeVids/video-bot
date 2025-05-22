# download.py
import feedparser
import yt_dlp
import os
import hashlib

DB_FILE = "posted.txt"


def get_top_wholesome_video():
    feed = feedparser.parse("https://www.reddit.com/r/wholesomevideos/.rss")
    for entry in feed.entries:
        if "youtu" in entry.link:
            vid_hash = hashlib.md5(entry.link.encode()).hexdigest()
            if not is_posted(vid_hash):
                mark_as_posted(vid_hash)
                return entry.link
    return None


def is_posted(vid_hash):
    if not os.path.exists(DB_FILE):
        return False
    with open(DB_FILE, 'r') as f:
        return vid_hash in f.read()


def mark_as_posted(vid_hash):
    with open(DB_FILE, 'a') as f:
        f.write(vid_hash + "\n")