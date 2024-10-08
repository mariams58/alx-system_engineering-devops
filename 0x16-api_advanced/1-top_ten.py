#!/usr/bin/python3
"""1-top_ten"""
import requests


def top_ten(subreddit):
    """Queries Reddit API and prints the titles for the top 10 hot post."""
    # Base URL for the Reddit API
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)

    # Set a custom User-Agent to avoid Too Many Requests error
    headers = {
        'User-Agent': '0x16-api:project:v1.0 (by /u/Broad_Advertising_21)'
    }
    params = {
        "limit": 10
    }
    # Make the request without following redirects
    response = requests.get(url, headers=headers,
                            params=params, allow_redirects=False)

    # Check if the request was successful (status code 200)
    if response.status_code != 200:
        print("None")
        return
    # Parse the JSON response data = response.json()
    posts = response.json().get('data').get('children')
    # Print the titles of the top 10 posts
    for post in posts:
        print(post.get('data').get('title'))
