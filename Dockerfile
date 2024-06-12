# Pull base image 
FROM python:3.12-slim-bullseye

# Set environment variables
ENV PIP_DISABLE_PIP_VERSION_CHECK 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /code


# Install dependencies
COPY requirement.txt ./
RUN pip install -r requirement.txt

# Copy project
COPY . .

EXPOSE 8000