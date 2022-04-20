#!/usr/bin/env python3

from utils.data import read_sample
from utils.labels import int_to_label
from utils.Tweet import tweet_to_string

"""
Utility for manually labelling data
"""


def labeller(input_file, output_file):
    """
    Labels tweets from an input file and writes them with their corresponding
    label to an output file. Labelled instances are removed from the input file.

    Parameters
    ----------
    input_file (str)
    output_file (str)

    Returns
    -------
    None
    """
    labelled_tweets = list()
    last_labelled_tweet = -1
    tweets = read_sample(input_file)
    try:
        for i, tweet in enumerate(tweets):
            print(f"{target - i} remaining")
            print(tweet.raw_content)
            c = input("Class: pu (1), pr (2), au (3), ar (4), n (5), us (6), u (7): ")
            print()
            tweet.label = int_to_label(int(c.strip()))
            labelled_tweets.append(tweet)
            last_labelled_tweet = i
    except (Exception, KeyboardInterrupt) as e:
        print(e)
    finally:
        print(f"Writing labelled tweets to {output_file}")
        with open(output_file, "a") as F:
            for tweet in labelled_tweets:
                F.write(tweet_to_string(tweet, label=True))
        print(f"Writing remaining tweets back into {input_file}")
        with open(input_file, "w") as F:
            for tweet in tweets[last_labelled_tweet + 1 :]:
                F.write(tweet_to_string(tweet))
    return None


if __name__ == "__main__":
    fname = "anti_russia"
    target = 250
    try:
        with open(f"data/labelled/{fname}.twint") as F:
            for line in F:
                target -= 1
    except FileNotFoundError:
        pass

    labeller(f"results/sia/{fname}.twint", f"data/labelled/{fname}.twint")
