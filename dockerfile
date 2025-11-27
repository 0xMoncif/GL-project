
# Use official Python 3.13 image
FROM python:3.13.7-slim

# Set working directory inside container
WORKDIR /app

# Install system dependencies for MySQL client and Pillow
RUN apt-get update && apt-get install -y \
    build-essential \
    default-libmysqlclient-dev \
    libjpeg-dev \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements file and install Python dependencies
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy the entire Django project into the container
COPY . .

# Expose the port Django will run on
EXPOSE 8000

# Run Django development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]




# to pass the env var when running docker u can do it with the cmd : docker run --env-file .env -p 8000:8000 dz-stagiaire-backend
# or implement it in docker compose so Docker automatically loads the environment variables from .env

