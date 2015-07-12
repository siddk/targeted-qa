"""
feature_extractor.py

File consisting of several feature extraction functions, used to create the representative feature
vector for a given query.
"""

from data

from spacy.en import English
nlp = English()

def build_keyword_counts(tokens):
    """Basic cue, extracts keyword counts in tokens, based on clusters in keywords.py"""


def build_feature_vector(sentence):
    """