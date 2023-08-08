#!/usr/bin/python3
"""a recursive function that queries the Reddit API, parses the title of all
hot articles, and prints a sorted count of given keywords (case-insensitive,
delimited by spaces. JS should count as javascript, but java should not).
"""
import requests


def count_words(subreddit, word_list, instances={}, after="", count=0):
    """Prints count of given arguments found in hot posts of a given subreddit.
    Args:
        subreddit (str): The subreddit to search.
        word_list (list): The list of words to search for in post titles.
        instances (obj): Key/value pairs of words/counts.
        after (str): The parameter for the next page of the API results.
        count (int): The parameter of results matched thus far.
    """
    if found_dict is None:
        found_dict = {}
    user_agent = {'User-agent': 'test45'}
    posts = requests.get('http://www.reddit.com/r/{}/hot.json?after={}'
                         .format(subreddit, after), headers=user_agent)
    if after is None:
        word_list = [word.lower() for word in word_list]

    if posts.status_code == 200:
        posts = posts.json()['data']
        aft = posts['after']
        posts = posts['children']
        for post in posts:
            title = post['data']['title'].lower()
            for word in title.split(' '):
                if word in word_list:
                    if word.lower() in found_dict.keys():
                        found_dict[word.lower()] += 1
                    else:
                        found_dict[word.lower()] = 1
        if aft is not None:
            count_words(subreddit, word_list, found_dict, aft)
        else:
            for key, value in sorted(found_dict.items(), key=lambda item: (item[1], item[0]), reverse=True):
                print('{}: {}'.format(key, value))
    else:
        return
