#!/usr/bin/env python3

"""
Class for storing Tweet data and converting to / from Twint format
"""

from .nlp import preprocess_text

from datetime import datetime

DELIMITER = " "
HASHTAG = "#"
TIMESTAMP_FORMAT = "%Y-%m-%d %H:%M:%S %z"


class Tweet:
    """
    Represents data from a Tweet returned from Twint
    """

    def __init__(self):
        """
        Initialize all attributes as None
        """
        self.id = None
        self.timestamp = None
        self.user = None
        self.sentiment = None
        self.label = None
        self.cluster = None
        self.cluster_distance = None
        self.raw_content = None
        self.tokenized_content = None
        self.hashtags = None
        self.is_english = None

    def __str__(self):
        return self.raw_content

    def __eq__(self, other):
        return self.id == other.id

    def __gt__(self, other):
        return self.timestamp > other.timestamp

    def __lt__(self, other):
        return self.timestamp < other.timestamp

    def __ge__(self, other):
        return self.timestamp >= other.timestamp

    def __le__(self, other):
        return self.timestamp <= other.timestamp


def string_to_tweet(tweet, label=False, cluster=False):
    """
    Converts a tweet from Twint into a Tweet object

    Parameters
    ----------
    tweet: str
        Tweet in Twint format
    label: bool
        If true, read label from tweet
    cluster: bool
        If true, read cluster from tweet

    Returns
    -------
    Tweet
    """
    data = Tweet()
    content = tweet.split(DELIMITER)
    data.id = content[0]
    data.timestamp = datetime.strptime(DELIMITER.join(content[1:4]), TIMESTAMP_FORMAT)
    data.user = content[4].replace("<", "").replace(">", "")
    if label and cluster:
        data.label = content[5].replace("[", "").replace("]", "")
        cluster_data = content[6].replace("{", "").replace("}", "").split(",")
        data.cluster = int(cluster_data[0])
        data.cluster_distance = float(cluster_data[1])
        data.raw_content = DELIMITER.join(content[7:])
    elif label:
        data.label = content[5].replace("[", "").replace("]", "")
        data.raw_content = DELIMITER.join(content[6:])
    elif cluster:
        cluster_data = content[5].replace("{", "").replace("}", "").split(",")
        data.cluster = int(cluster_data[0])
        data.cluster_distance = float(cluster_data[1])
        data.raw_content = DELIMITER.join(content[6:])
    else:
        data.raw_content = DELIMITER.join(content[5:])
    data.tokenized_content = preprocess_text(data.raw_content)
    data.hashtags = generate_list_of_hashtags(data.raw_content)
    data.is_english = True
    return data


def generate_list_of_hashtags(content):
    """
    Converts hashtags in a tweet to a list of words without an octothorpe prefix

    Parameters
    ----------
    content: str
        Raw content of tweet

    Returns
    -------
    Collection
        List of hashtags without octothorpe prefix
    """
    hashtags = list()
    for word in content.split(DELIMITER):
        if content[0] == HASHTAG:
            hashtags.append(content[1:])
    return hashtags


def tweet_to_string(d, label=False, cluster=False):
    """
    Convert a Tweet object containing tweet data into a string

    Parameters
    ----------
    d: Tweet
        Format generated from string_to_tweet
    label: bool
        If true, include label
    cluster: bool
        If true, include cluster

    Returns
    -------
    str
    """
    if label and cluster:
        label_content = d.label
        cluster_content = f"{d.cluster},{d.cluster_distance}"
        return " ".join(
            [
                d.id,
                datetime.strftime(d.timestamp, TIMESTAMP_FORMAT),
                f"<{d.user}>",
                f"[{label_content}]",
                "{" + cluster_content + "}",
                d.raw_content,
            ]
        )
    elif label:
        label_content = d.label
        return " ".join(
            [
                d.id,
                datetime.strftime(d.timestamp, TIMESTAMP_FORMAT),
                f"<{d.user}>",
                f"[{label_content}]",
                d.raw_content,
            ]
        )
    elif cluster:
        cluster_content = f"{d.cluster},{d.cluster_distance}"
        return " ".join(
            [
                d.id,
                datetime.strftime(d.timestamp, TIMESTAMP_FORMAT),
                f"<{d.user}>",
                "{" + str(cluster_content) + "}",
                d.raw_content,
            ]
        )

    else:
        return " ".join([d.id, datetime.strftime(d.timestamp, TIMESTAMP_FORMAT), f"<{d.user}>", d.raw_content])
