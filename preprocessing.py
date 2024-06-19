# -*- coding: utf-8 -*-
"""DhruvMiyani_Project_OA.ipynb

##Part 1 - Generating Embeddings
Determine an appropriate model to generate embeddings for the job descriptions. It can be pre-trained models like Sentence Transformers, GloVe, FastText, Word2Vec, Doc2Vec, CBOW, skip-gram, or any other approach you think would be best suited.
Justify your choice: Explain why you chose this method and its potential advantages for this task and its potential advantages in the context of duplicate detection.
Generate embeddings for each job description in the dataset.

### Imports
"""
import pandas as pd
from bs4 import BeautifulSoup
from sentence_transformers import SentenceTransformer
import csv
import torch
#from IPython.display import FileLink

"""### Data Preprocessing"""


"""#### Skipping Some Troubeling Rows - Error while Reading DataFrame"""

def clean_csv(file_path):
    with open(file_path, 'r', encoding='utf-8') as infile, open('cleaned_file.csv', 'w', encoding='utf-8', newline='') as outfile:
        reader = csv.reader(infile)
        writer = csv.writer(outfile)
        for row in reader:
            try:
                writer.writerow(row)
            except Exception as e:
                print(f"Skipping row due to error: {e}")

clean_csv('jobpostings.csv')

print("if this throwing error use files/cleaned_file.csv")
cleaned_df =pd.read_csv('cleaned_file.csv')

job_descriptions = cleaned_df['Job Description'].tolist()

job_descriptions[1]

"""#### Removing HTML tags"""



def clean_html(raw_html):
    clean_text = BeautifulSoup(raw_html, 'html.parser').get_text()
    return clean_text

# Filter out non-string entries
filtered_descriptions = [desc for desc in job_descriptions if isinstance(desc, str)]

# Clean the job descriptions
cleaned_descriptions = [clean_html(desc) for desc in filtered_descriptions]

print(cleaned_descriptions)

cleaned_descriptions[1]

"""###  Generating Embeddings Using SentenceTransformer"""



# Load the pre-trained model
model = SentenceTransformer('all-MiniLM-L6-v2')


# Generate embeddings
embeddings = model.encode(cleaned_descriptions)

#from google.colab import files

print("if this throwing error use files/job_description_embeddings.pt")
embedding_file_path = "../embedding/job_description_embeddings.pt"
torch.save(embeddings, embedding_file_path)
#files.download(embedding_file_path)

# I done this part using T4 processor - google colab  - to save time 
