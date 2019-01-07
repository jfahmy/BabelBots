# Use an official Python runtime as a parent image
FROM python:2.7-slim

# Set the working directory
ADD . /

# Copy the current directory contents into the container at /app
# COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install grpc
RUN pip install grpcio-tools
RUN pip install tweepy


# Make port available to the world outside this container?
EXPOSE 50050

# Define environment variable
# ENV NAME World

# Run this when the container launches
CMD ["python", "BotQuixotic.py"]
