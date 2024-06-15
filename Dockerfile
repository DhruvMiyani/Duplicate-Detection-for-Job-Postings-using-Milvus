
# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy the requirements file into the container at /usr/src/app
COPY requirements.txt ./

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the working directory contents into the container at /usr/src/app
COPY . .

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Define environment variable
ENV NAME World

# Run server.py when the container launches
#CMD ["python", "server.py"]
CMD ["sh", "-c", "detect_duplicates.py"]


#FROM python:3.7

#WORKDIR /app

#COPY . /app

#RUN pip install --no-cache-dir -r requirements.txt

#EXPOSE 80

#ENV NAME job_post_duplicate_detection

# Run generate_embeddings.py when the container launches
#CMD ["sh", "-c", "python preprocessing.py && python detect_duplicates.py"]
