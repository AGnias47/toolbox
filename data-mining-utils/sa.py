#!/usr/bin/env python3

"""
Script for performing sentiment analysis on a sample
"""

from nltk.sentiment.vader import SentimentIntensityAnalyzer
import tqdm


def sentiment_intensity_analyzer(sample):
    """
    Separates sample into three separate lists of positive, negative, and neutral

    Parameters
    ----------
    sample: Collection

    Returns
    -------
    list, list, list
        positive, negative, and neutral entries, respectively
    """
    sid = SentimentIntensityAnalyzer()
    pos, neg, neu = list(), list(), list()
    for text in tqdm.tqdm(sample):
        compound_score = sid.polarity_scores(text.raw_content)["compound"]
        if compound_score > 0:
            pos.append(text)
        elif compound_score < 0:
            neg.append(text)
        else:
            neu.append(text)
    pos = sorted(pos, key=lambda x: x.sentiment, reverse=True)
    neg = sorted(neg, key=lambda x: x.sentiment, reverse=False)
    return pos, neg, neu
