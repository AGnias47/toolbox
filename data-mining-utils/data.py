#!/usr/bin/env python3

"""
Functions for handling sample data
"""

from .Tweet import string_to_tweet, tweet_to_string
import random
import tqdm

DELIMITER = " "
HASHTAG = "#"
TIMESTAMP_FORMAT = "%Y-%m-%d %H:%M:%S %z"
LANGUAGE = "english"


def read_sample(sample, label=False, cluster=False, shuffle=False, limit=999999999):
    """
    Read twint data from a file and convert into a list of dicts

    Parameters
    ----------
    sample: str
        filename
    label: bool
        If true, parse labels from sample
    cluster: bool
        If true, parse clusters from sample
    shuffle: bool
        If true, shuffle the sample
    limit (default is 999999999): int
        Limit sample to x amount of tweets

    Returns
    -------
    Collection
        List of tweets as dicts
    """
    samples = list()
    with open(sample) as F:
        print(f"Reading sample from {sample}")
        for i, line in tqdm.tqdm(enumerate(F)):
            try:
                tweet = string_to_tweet(line, label, cluster)
            except ValueError:
                print("Value Error")
                continue
            samples.append(tweet)
            if i > limit:
                break
    if shuffle:
        random.shuffle(samples)
    return samples


def write_sample(fname, tweets, label=False, cluster=False):
    """
    Writes a sample stored as a list of dicts to a file

    Parameters
    ----------
    fname: str
        Path to write file
    tweets: list
        List of tweets to write to file
    label (default is False): bool
        If True, include label in file
    cluster (default is False): bool
        If True, include cluster in file

    Returns
    -------
    None
    """
    print(f"Writing file to {fname}")
    with open(fname, "w") as F:
        for tweet in tqdm.tqdm(tweets):
            F.write(tweet_to_string(tweet, label, cluster))
            F.write("\n")
    return None
