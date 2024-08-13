#!/usr/bin/python3
import requests

def number_of_subscribers(subreddit):
    """
    Returns the number of subscribers for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit.  


    Returns:
        int: The number of subscribers, or 0 if the subreddit is invalid.
    """

    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'your_user_agent'}  # Replace with your custom User-Agent

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise an exception for error HTTP statuses

        data = response.json()
        return data['data']['subscribers']
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data for subreddit {subreddit}: {e}")
        return 0
