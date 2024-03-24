import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
import spacy
from Course_Webscrapping_and_Dataframe import data_science
from Course_Webscrapping_and_Dataframe import immersive_tech
from Course_Webscrapping_and_Dataframe import comp_arts
from Course_Webscrapping_and_Dataframe import soc

# Sample course descriptions
course_descriptions = [
    "CSC446: Artificial intelligence. Learn about AI and the tools.",
    "CSC550: Machine Learning. Introduction to ML algorithms and applications.",
    "CSC660: Natural Language Processing. Study of NLP techniques and applications.",
    "CSC732: Deep Learning. Dive into deep learning concepts and architectures.",
    "CSC810: Computer Vision. Introduction to computer vision algorithms and frameworks.",
    "ARH325: Modern Architecture. Learn about Le Corbusier's design principles.",
    "ABC224: Animal Husbandry. Course about the history and development of animal husbandry.",
    "PHIL332: Justice and Virtue. Dr. Bryan teaches the theory behind famous philosophies about justice."
]

# Load Spacy model
nlp = spacy.load("en_core_web_lg")

# Function to embed text using Spacy model
def embed_text(text):
    return nlp(text).vector

# Embed course descriptions
course_embeddings = [embed_text(desc) for desc in course_descriptions]

def find_matching_courses(search_description, num_courses=5):
    # Embed search description
    search_embedding = embed_text(search_description)

    # Compute cosine similarity between search description and course descriptions
    similarities = cosine_similarity([search_embedding], course_embeddings)[0]

    # Sort indices of courses by similarity
    sorted_indices = np.argsort(similarities)[::-1]

    # Get top matching courses
    top_matches = [(course_descriptions[idx], similarities[idx]) for idx in sorted_indices[:num_courses]]

    return top_matches

# Sample search description
search_description = "nlp"

# Get top matching courses
top_matches = find_matching_courses(search_description, 5)

# Print top matching courses
print("Top matching courses:")
for course, similarity in top_matches:
    print(f"Course: {course}, Similarity: {similarity}")