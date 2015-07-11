# Targeted Question-Answering #
This repository contains a natural language question-answering system for my personal site. It reads in a user 
question, parses out the information, and directs them to the relevant section of the website. For example, if 
a question reads "Tell me about yourself, Sidd", it will direct them to the "About" section of my website.

I'm particularly passionate about natural language processing, and after completing a series of related projects
at school and at work, I wanted to work on something like this on the side, to see how building a classification
algorithm like this off a small test-set can improve drastically over time, as more data comes in.

### Continuous Learning ###
At first, this model and classification algorithm is going to have vastly sub-par results. This is because, at least 
to start with, the number of examples really won't be enough to build up a meaningful test set. That being said, this
is an exercise to both see how my personal understanding of natural language improves over time, and to see how an 
influx of new data improves the model. This is done in the following manner:

First, as more people visit my personal web page and query the system to direct them to the relevant session, the hope
is that the model will continue to improve. It does this by logging all input queries to a database, tagging them with 
the target location that the user actually visits. The model is then retrained (for now, weekly, as I'm not expecting 
much traffic).

Second, as I continue to study the field, the hope is that I will begin to see different ways to improve the existing
framework, either by adapting the existing feature methods, or by extracting new features altogether. 

### Model Explanation ###
To build this classification model, I first extract a set of features from a series of test
questions (with each question tagged with the section it refers to). Then, I train a classifier using a MultiClass
Perceptron that I built ([check it out here](https://github.com/siddk/multiclass_perceptron)), returning a classifier 
to be used for dynamic prediction (as new queries come in).

On the actual site, the classifier pipeline is running as part of a Python Flask app. When a query comes in, the 
feature extractor is run, extracting the desired features, returning a feature vector. This feature vector is then
piped to the classifier, which returns the predicted section.

---------------------------------------------------------------------------------------------------------------------

Again, this is by no means going to start off as a perfect algorithm - in fact, it is probably going to have some
pretty terrible results to start with. However, as more and more data comes in, and as I learn more about natural 
language processing, I do hope I will start to see drastic improvement.

