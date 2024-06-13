# MilvusProject


## Introduction

The project focuses on the following key tasks:

1. **Data Preprocessing:**  Clean job postings data, handling missing values , removing HTML tags 
2. **Generating Embeddings:** Used a pre-trained model Sentence Transformers to generate embeddings 
3. **Milvus for Duplicate Detection:** Set up a Milvus instance, insert embeddings, and implement a method to search for potential duplicates.
4. **Docker/Docker Compose Integration:** Containerize the project for easy reproducibility.



## Project Structure

```plaintext
/MilvusProject
|-- job_postings.csv/
|-- preprocessing.py/
|-- detect_duplicates.py/
|-- embeddings/
|   |-- job_description_embeddings.pt
|-- files/
|   |-- cleaned_file.py
|   |-- embedding_csv.py
|-- Dockerfile
|-- docker-compose.yml
|-- README.md
```



## Requirements

- Python 3.x
- PyTorch
- Sentence Transformers
- pymilvus



Install dependencies using:

```bash
pip install -r requirements.txt
```



## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/DhruvMiyani/MilvusProjectMLeng.git
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```



## Usage

1. **Data Preprocessing:**

   Explore and clean the data in the `job_postings.csv` file.

2. **Generating Embeddings:**

   Run the following command to generate embeddings:

   ```bash
   python preprocessing.py
   ```

3. **Milvus for Duplicate Detection:**

   - Set up Milvus instance and duplicate detection:

     ```bash
     python milvus/duplicate_detection.py
     ```

4. **Docker/Docker Compose Integration:**

   - Build and run the Docker image:

     ```bash
     docker build -t MilvisProject
     docker-compose up
     ```


## Docker Integration

The project includes Docker and Docker Compose files (`Dockerfile` and `docker-compose.yml`) for containerization. This ensures a reproducible and isolated environment.

To build and run the Docker image, follow the instructions in the [Usage](#usage) section.

