# Use the Python slim base image
FROM python:3.9-slim

# Update OS packages
RUN apt-get update && apt-get upgrade -y && apt-get clean

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app
COPY requirements.txt /app

# Set PYTHONPATH to find our Python modules
ENV PYTHONPATH=/app
ENV 1PTOKEN=None
ENV PYTHONBUFFERED=1

# Install any needed dependencies specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 80 to the outside world
EXPOSE 80

# Command to run the FastAPI application
CMD ["uvicorn", "myfastapi.app:app", "--host", "0.0.0.0", "--port", "80", "--reload"]
