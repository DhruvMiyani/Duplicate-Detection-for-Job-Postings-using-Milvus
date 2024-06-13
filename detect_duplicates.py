

from pymilvus import MilvusClient
import torch
import numpy as np

# Connect to Milvus
client = MilvusClient("job_description.db")

# Create a collection
collection_name = "job_description_collection"
dimension = 384
client.create_collection(
    collection_name=collection_name,
    dimension=dimension,
)

# Load embeddings
print("if you are getting error here , try this for path ","../embedding/job_description_embeddings_2.pt")
embedding_file_path = "embeddings/job_description_embeddings.pt"
embeddings = torch.load(embedding_file_path)
print("Shape of embeddings:", embeddings.shape)

# Insert data into the collection
data = [{"id": i, "vector": embeddings[i].tolist()} for i in range(len(embeddings))]
client.insert(collection_name=collection_name, data=data)


def cosine_similarity(a, b):
    dot_product = np.dot(a, b)
    norm_a = np.linalg.norm(a)
    norm_b = np.linalg.norm(b)
    return dot_product / (norm_a * norm_b)

# Detect duplicates
duplicates = []
ids = []
vectors = []
threshold = 0.9
for i in range(len(data)):
    vector = np.array(data[i]["vector"])
    for j in range(len(vectors)):
        similarity = cosine_similarity(vector, vectors[j])
        if similarity > threshold:
            duplicates.append((i, ids[j], similarity))
    ids.append(data[i]["id"])
    vectors.append(vector)

print("Duplicates:", duplicates)
