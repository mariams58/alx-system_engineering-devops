#!/usr/bin/python3
"""Function to query subscriber on a given reddit"""
import requests


def number_of_subscribers(subreddit):
    """
    Queries the Reddit API and returns the
    number of subscribers for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit.

    Returns:
        int: The number of subscribers, or 0 if the subreddit is invalid.
    """
    # Base URL for the Reddit API
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)

    # Set a custom User-Agent to avoid Too Many Requests error
    headers = {
        'User-Agent': 'Deedee User Agent 1.0'
    }
    # Make the request without following redirects
    response = requests.get(url, headers=headers, allow_redirects=False)

    # Check if the request was successful (status code 200)
    if response.status_code != 200:
        return 0
    # Parse the JSON response
    data = response.json().get('data').
    # Return the number of subscribers
    return data.get('subscribers')
