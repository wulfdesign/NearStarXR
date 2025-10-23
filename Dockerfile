# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy the requirements file into the container
COPY server/requirements.txt ./

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the server and app directories into the container
COPY ./server /usr/src/app/server
COPY ./app /usr/src/app/app

# Run the data processing script
RUN python server/process_data.py

# Make port 8080 available to the world outside this container
EXPOSE 8080

# Define environment variable
ENV PORT 8080

# Run main.py when the container launches
CMD ["gunicorn", "--bind", "0.0.0.0:8080", "server.main:app"]