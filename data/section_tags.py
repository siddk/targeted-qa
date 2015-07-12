"""
section_tags.py

Example queries tagged with the respective section, for use in training the QA classifier.
"""

# Feature list
feature_list = ["about_keywords", "education_keywords", "work_keywords", "project_keywords",
                "why", "who", "where", "what", "how"]

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
           ("about", "Why are you at Brown?"),
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
           ("education", "Education"),
           ("education", "School"),
           ("work", "Where do you work?"),
           ("work", "Where have you worked?"),
           ("work", "How was AutoGrid?"),
           ("work", "How was 61A?"),
           ("work", "How was WriteLab?"),
           ("work", "Work"),
           ("work", "Work Experience"),
           ("work", "What work have you done?"),
           ("work", "How was the Par Lab?"),
           ("work", "How was the Oscii Lab?"),
           ("work", "What research have you done?"),
           ("work", "What are you researching?"),
           ("projects", "Project"),
           ("projects", "Projects"),
           ("projects", "What are some of your projects?"),
           ("projects", "What are some of your hobbies"),
           ("projects", "What do you do in your free time")]