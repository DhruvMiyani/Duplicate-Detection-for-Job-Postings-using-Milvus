# MilvusProject


## Introduction

The project focuses on the following key tasks:

1. **Data Preprocessing:**  Clean job postings data, handling missing values , removing HTML tags 
2. **Generating Embeddings:** Used a pre-trained model Sentence Transformers to generate embeddings 
3. **Milvus for Duplicate Detection:** Set up a Milvus instance, insert embeddings, and implement a method to search for potential duplicates.
4. **Docker/Docker Compose Integration:** Containerize the project for easy reproducibility.

## Demo:

https://drive.google.com/file/d/15rrFDdftzcWTLXRy5gJbzYsBdPyZLvmA/view?usp=sharing


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



## Installation and Docker Compose Integration

1. Clone the repository:

   ```bash
   git clone https://github.com/DhruvMiyani/MilvusProjectMLeng.git
   ```

3. Start Milvis:

   ```bash
   bash standalone_embed.sh start
   ```
4. Build Image:

   ```bash
   docker build -t milvus2:latest .
   ```

4. Run:

   ```bash
   docker run -p 80:80 milvus2
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

## Docker Integration

The project includes Docker and Docker Compose files (`Dockerfile` and `docker-compose.yml`) for containerization. This ensures a reproducible and isolated environment.

To build and run the Docker image, follow the instructions in the [Usage](#usage) section.

