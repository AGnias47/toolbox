#!/usr/bin/env python3

"""
Natural Language Processing functions
"""

from string import punctuation
import nltk
import nltk.corpus
from nltk.stem import SnowballStemmer

LANGUAGE = "english"


def is_english(text):
    """
    Too inefficient to effectively use. Recommend grepping for non-english chars with:
    grep -Pv "[\x80-\xFF]"

    Parameters
    ----------
    text

    Returns
    -------
    bool
    """
    english_words = set(nltk.corpus.words.words())
    text_as_list = [c for c in text.lower() if c not in punctuation and c[0:4] != "http" or not c.isalpha()]
    english = 0
    non_english = 0
    for word in text_as_list:
        if word in english_words:
            english += 1
        else:
            non_english += 0
    try:
        return english / (english + non_english) > 0.667
    except ZeroDivisionError:
        return False


def preprocess_text(content):
    """
    Preprocesses text for NLP analysis.
    Followed preprocessing procedure from:
    https://towardsdatascience.com/nlp-preprocessing-with-nltk-3c04ee00edc0

    Parameters
    ----------
    content: str
        text to process

    Returns
    -------
    Collection
    """
    # Convert to lowercase, remove punctuation and URLs
    content = "".join([c for c in content.lower() if c not in punctuation and c[0:4] != "http"])
    # Tokenize
    content = nltk.word_tokenize(content, language=LANGUAGE)
    # Remove stopwords
    content = [t for t in content if t not in nltk.corpus.stopwords.words(LANGUAGE)]
    # Stem via SnowballStemmer
    stemmer = SnowballStemmer(LANGUAGE)
    content = [stemmer.stem(t) for t in content]
    return content
