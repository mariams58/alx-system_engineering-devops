#!/usr/bin/python3
"""2-recursive"""
import requests


def recurse(subreddit, hot_list=[]):
    """
    Queries the Reddit API recursively and returns a listr
    containing tiotles of all hot articles

    Args:
        subreddit (str): The name of the subreddit.
        hot_list (list): the list of aricles

    Returns:
    list: a list of alltitles
    """
    # Base URL for the Reddit API
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)

    # Set a custom User-Agent to avoid Too Many Requests error
    headers = {'User-Agent': '0x16-api:project:v1.0 (by /u/Broad_Advertising_21)'}

    # Parameters for pagination
    params = {
        'limit': 100,
        'after': after,
        'count': count
    }

    # Make the request without following redirects
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)

    # Check if the request was not successful (status code 200)
    if response.status_code != 200:
        return None
    # Parse the JSON response
    data = response.json().get('data')
    after = data.get("after")
    children = data.get('children')
    # Extract titles of hot articles
    for child in children:
        hot_list.append(child.get('data', {}).get('title'))
    # checks for next page 
    if after is not None:
        return recurse(subreddit, hot_list, after, count)
    return hot_list
