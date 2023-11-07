#!/usr/bin/python3
"""Script to get top 10 hot posts on a subreddit"""

import requests


def top_ten(subreddit):
    """a function that queries the Reddit API and prints
    the titles of the first 10 hot
    posts listed for a given subreddit."""

    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=9"
    response = requests.get(url, headers={'User-Agent': 'app/1.0'})
    data = response.json()

    # Print the response data
    posts = data['data']['children']
    for post in posts:
        return post['data']['title']

# if __name__ == '__main__':
#     # Example: Get the response structure for the "programming" subreddit
#     subreddit_name = 'programming'
#     top_ten(subreddit_name)
