"""
File of tagged key words, for building syn-sets, large scale representative vectors, etc.

Built by looking through Wordnet and Spacy repvecs and taking the top n most common words in existing
webpage source per section.
"""

about_keywords = ["about", "interests", "transfer", "leave", "from"]

education_keywords = ["education", "school", "college", "university", "learn", "berkeley",
                      "brown", "academic", "academics", "courses", "classes", "schoolwork",
                      "major", "majoring", "concentrate", "concentrating", "studying", "study"]

work_keywords = ["work", "experience", "research", "researching", "working", "lab", "oscii",
                 "par", "write", "writelab", "autogrid", "grid", "auto", "61a", "ta", "teach",
                 "teaching", "skills"]

project_keywords = ["project", "projects", "hobby", "hobbies", "free", "time", "papers", "paper",
                    "portfolio", "showcase"]