#!/bin/usr/python3
"""
1-top_ten
"""
import requests


def top_ten(subreddit):
    """
    Queries the Reddit API and returns the titles for
    the top ten hot post for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit.

    Returns:
        int: The number of subscribers, or 0 if the subreddit is invalid.
    """
    # Base URL for the Reddit API
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10n"

    # Set a custom User-Agent to avoid Too Many Requests error
    # headers = {'User-Agent': 'python:subreddit
    # .subscriber.count:v1.0 (by /u/yourusername)'}

    try:
        # Make the request without following redirects
        response = requests.get(url, allow_redirects=False)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the JSON response
            data = response.json()
            posts = data.get('data', {}).get('children', [])
            # Print the titles of the top 10 posts
            for post in posts:
                print(post.get('data', {}).get('title'))
        else:
            # Prints None if the subreddit is invalid or there's an error
            print(None)
    except requests.RequestException:
        # Prints None in case of a network-related error
        print(None)
