# Pull base image
FROM python:3.6.10

# Set environment varibles
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /code

# Copy project
COPY . /code/
RUN pip install --upgrade pip

# Install dependencies
RUN pip install -r requirements.txt
