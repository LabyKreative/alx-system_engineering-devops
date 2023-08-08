#!/usr/bin/python3
"""a recursive function that queries the Reddit API, parses the title of all
hot articles, and prints a sorted count of given keywords (case-insensitive,
delimited by spaces. JS should count as javascript, but java should not).
"""
import json
import requests


def count_words(subreddit, word_list, after="", count=[]):
    """Prints count of given arguments found in hot posts of a given subreddit.
    Args:
        subreddit (str): The subreddit to search.
        word_list (list): The list of words to search for in post titles.
        instances (obj): Key/value pairs of words/counts.
        after (str): The parameter for the next page of the API results.
        count (int): The parameter of results matched thus far.
    """
    if after == "":
        count = [0] * len(word_list)

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    request = requests.get(url,
                           params={'after': after},
                           allow_redirects=False,
                           headers={'user-agent': 'bhalut'})

    if request.status_code == 200:
        data = request.json()

        for topic in (data['data']['children']):
            for word in topic['data']['title'].split():
                for x in range(len(word_list)):
                    if word_list[x].lower() == word.lower():
                        count[x] += 1

        after = data['data']['after']
        if after is None:
            save = []
            for x in range(len(word_list)):
                for y in range(x + 1, len(word_list)):
                    if word_list[x].lower() == word_list[y].lower():
                        save.append(j)
                        count[x] += count[y]

            for x in range(len(word_list)):
                for y in range(x, len(word_list)):
                    if (count[y] > count[x] or
                            (word_list[x] > word_list[y] and
                             count[y] == count[x])):
                        aux = count[x]
                        count[x] = count[y]
                        count[y] = aux
                        aux = word_list[x]
                        word_list[x] = word_list[y]
                        word_list[y] = aux

            for x in range(len(word_list)):
                if (count[x] > 0) and x not in save:
                    print("{}: {}".format(word_list[x].lower(), count[x]))
        else:
            count_words(subreddit, word_list, after, count)
