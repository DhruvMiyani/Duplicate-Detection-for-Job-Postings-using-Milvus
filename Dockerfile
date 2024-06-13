FROM python:3.8-slim

WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt

ENV NAME job_post_duplicate_detection

# Run generate_embeddings.py when the container launches
CMD ["sh", "-c", "python ./preprocessing.py && python ./detect_duplicates.py"]

