import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
import spacy

# Load Spacy model
nlp = spacy.load("en_core_web_lg")

def get_course_descriptions():
    data_course_descript = []
    immers_course_descript = []
    arts_course_descript = []
    soc_course_descript = []

    #Using relative path .\\
    data_file = open('.\\data_courses.txt', 'r')
    for line in data_file:
        line = line.strip().split(' : ')
        data_course_descript.append(line[0] + " : " + line[1].lower())
    data_file.close()

    immersive_file = open('.\\immersive_courses.txt', 'r')
    for line in immersive_file:
        line = line.strip().split(' : ')
        immers_course_descript.append(line[0] + " : " + line[1].lower())
    immersive_file.close()
    
    arts_file = open('.\\arts_courses.txt', 'r')
    for line in arts_file:
        line = line.strip().split(' : ')
        arts_course_descript.append(line[0] + " : " + line[1].lower())
    arts_file.close()

    society_file = open('.\\soc_courses.txt', 'r')
    for line in society_file:
        line = line.strip().split(' : ')
        soc_course_descript.append(line[0] + " : " + line[1].lower())
    society_file.close()
   
    return  data_course_descript, immers_course_descript, arts_course_descript, soc_course_descript


# Function to embed text using Spacy model
def embed_text(text):
    return nlp(text).vector


def find_matching_data_courses(search_description, data_courses, num_courses=5):
    # Embed search description
    search_embedding = embed_text(search_description)

    # Embed course descriptions
    course_embeddings = [embed_text(desc) for desc in data_courses]

    # Compute cosine similarity between search description and course descriptions
    similarities = cosine_similarity([search_embedding], course_embeddings)[0]

    # Sort indices of courses by similarity
    sorted_indices = np.argsort(similarities)[::-1]

    # Get top matching courses
    top_matches = [(data_courses[idx], similarities[idx]) for idx in sorted_indices[:num_courses]]

    return top_matches

def find_matching_immersive_courses(search_description, immersive_courses, num_courses=5):
    # Embed search description
    search_embedding = embed_text(search_description)

    # Embed course descriptions
    course_embeddings = [embed_text(desc) for desc in immersive_courses]

    # Compute cosine similarity between search description and course descriptions
    similarities = cosine_similarity([search_embedding], course_embeddings)[0]

    # Sort indices of courses by similarity
    sorted_indices = np.argsort(similarities)[::-1]

    # Get top matching courses
    top_matches = [(immersive_courses[idx], similarities[idx]) for idx in sorted_indices[:num_courses]]

    return top_matches

def find_matching_arts_courses(search_description, arts_courses, num_courses=3):
    # Embed search description
    search_embedding = embed_text(search_description)

    # Embed course descriptions
    course_embeddings = [embed_text(desc) for desc in arts_courses]

    # Compute cosine similarity between search description and course descriptions
    similarities = cosine_similarity([search_embedding], course_embeddings)[0]

    # Sort indices of courses by similarity
    sorted_indices = np.argsort(similarities)[::-1]

    # Get top matching courses
    top_matches = [(arts_courses[idx], similarities[idx]) for idx in sorted_indices[:num_courses]]

    return top_matches

def find_matching_society_courses(search_description, society_courses, num_courses=3):
    # Embed search description
    search_embedding = embed_text(search_description)

    # Embed course descriptions
    course_embeddings = [embed_text(desc) for desc in society_courses]

    # Compute cosine similarity between search description and course descriptions
    similarities = cosine_similarity([search_embedding], course_embeddings)[0]

    # Sort indices of courses by similarity
    sorted_indices = np.argsort(similarities)[::-1]

    # Get top matching courses
    top_matches = [(society_courses[idx], similarities[idx]) for idx in sorted_indices[:num_courses]]

    return top_matches




def main():
    # Sample search description
    data_search_description = "machine learning artificial intelligence data science"
    immersive_search_description = "human computer interaction creative code"
    arts_search_description = "arts"
    society_search_description = "identity"
    data, immersive, arts, society = get_course_descriptions()
    top_data_matches = find_matching_data_courses(data_search_description, data, 5)
    
    top_immersive_matches = find_matching_immersive_courses(immersive_search_description, immersive, 5)

    top_arts_matches = find_matching_arts_courses(arts_search_description, arts, 3)
    top_society_matches = find_matching_society_courses(society_search_description, society, 3)
    # Print top matching courses
    print("Top matching courses:")
    for course, similarity in top_arts_matches:
        print(f"Course: {course}, Similarity: {similarity}")
    


main()