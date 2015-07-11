"""
section_tags.py

Example queries tagged with the respective section, for use in training the QA classifier.
"""

# Different categories data is broken up into.
sections = ["about", "education", "work", "projects"]

queries = [("about", "Tell me about yourself"),
           ("about", "Tell me about yourself, Sidd"),
           ("about", "About"),
           ("about", "Who are you?"),
           ("about", "What are your interests?"),
           ("about", "Where are you from?"),
           ("about", "What do you do?"),
           ("about", "What inspires you?"),
           ("about", "Why did you leave Berkeley?"),
           ("about", "Why did you transfer?"),
           ("about", "")
    ("education", "Where did you go to school?"),
    ("education", "Where do you go to school?"),
    ("education", "Where did you go to college?"),
    ("education", "Where do you go to college?"),
    ("education", "What do you study?"),
    ("education", "What are you studying?"),
    ("education", "What is your major?"),
    ("education", "What are you concentrating in?"),
    ("education", "What is your concentration?"),
    ("education", "How was Berkeley?"),
    ("education", "How is Brown?"),
    ]