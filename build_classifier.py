"""
build_classifier.py

Build classifier object, save it as a pickle file.
"""
from multiclass_perceptron.mc_perceptron import MultiClassPerceptron
from data.section_tags import queries, feature_list, sections
from feature_extractor import build_feature_vector
import cPickle as pickle


def build_classifier():
    """Build and pickle the classifier."""
    classes = sections
    feature_data = [(tag, build_feature_vector(s)) for (tag, s) in queries]

    classifier = MultiClassPerceptron(classes, feature_list, feature_data, train_test_ratio=1)
    classifier.train()

    with open("classifier.pik", 'wb') as f:
        pickle.dump(classifier, f, pickle.HIGHEST_PROTOCOL)


def load_classifier():
    """
    Load classifier from pickle file, return as object

    :return: MultiClassPerceptron class object
    """
    with open("classifier.pik", 'rb') as f:
        return pickle.load(f)


def predict_section(classifier, sentence):
    """
    Given an input section

    :param classifier  Classifier to use for prediction
    :param sentence    Sentence to run prediction on
    :return            Return predicted section
    """
    feature_vector = build_feature_vector(sentence)
    return classifier.predict(feature_vector)


# Main Method
if __name__ == "__main__":
    build_classifier()
    c = load_classifier()
    print "Section: ", predict_section(c, "Why did you leave Berkeley?")