"""
feature_extractor.py

File consisting of several feature extraction functions, used to create the representative feature
vector for a given query.
"""

from data.keywords import about_keywords, education_keywords, work_keywords, project_keywords
from spacy.en import English
nlp = English()

feature_list = ["about_keywords", "education_keywords", "work_keywords", "project_keywords",
                "why", "who", "where", "what", "how"]


def build_keyword_counts(tokens, feature_dict):
    """
    Basic cue, extracts keyword counts in tokens, based on clusters in keywords.py.

    :param tokens        List of spacy tokens to parse for keywords
    :param feature_dict  Feature dictionary (to append to)
    """
    for t in tokens:
        tok = t.string.strip().lower()
        if tok in about_keywords:
            feature_dict["about_keywords"] += 1
        elif tok in education_keywords:
            feature_dict["education_keywords"] += 1
        elif tok in work_keywords:
            feature_dict["work_keywords"] += 1
        elif tok in project_keywords:
            feature_dict["project_keywords"] += 1


def build_qword_counts(tokens, feature_dict):
    """
    Extracts question word counts in tokens, adds to feature_dict.

    :param tokens:       List of spacy tokens to parse for keywords
    :param feature_dict  Feature dictionary (to append to)
    """
    for t in tokens:
        tok = t.string.strip().lower()
        if tok == "why":
            feature_dict["why"] += 1
        elif tok == "who":
            feature_dict["who"] += 1
        elif tok == "where":
            feature_dict["where"] += 1
        elif tok == "what":
            feature_dict["what"] += 1
        elif tok == "how":
            feature_dict["how"] += 1


def build_feature_vector(sentence):
    """
    Build feature dictionary mapping feature name to numeric value.

    :param sentence  Sentence to parse
    :return          Return feature vector (as dictionary)
    """
    tokens = nlp(unicode(sentence))
    feature_dictionary = {feature: 0 for feature in feature_list}

    build_keyword_counts(tokens, feature_dictionary)
    build_qword_counts(tokens, feature_dictionary)

    return feature_dictionary