# Use an official Python runtime as a parent image
FROM python:3.9.6-slim

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Authentication and Authorization
ENV ACCESS_TOKEN_EXPIRE_MINUTES=$ACCESS_TOKEN_EXPIRE_MINUTES
ENV SECRET_KEY=$SECRET_KEY
ENV ALGORITHM=$ALGORITHM

# Files
ENV DROPBOX_ACCESS_TOKEN=$DROPBOX_ACCESS_TOKEN

# Database
ENV DATABASE_URI=$DATABASE_URI

# Email
ENV SMTP_LOGIN=$SMTP_LOGIN
ENV SMTP_PASSWORD=$SMTP_PASSWORD
ENV SMTP_API_KEY=$SMTP_API_KEY
ENV EMAILS_FROM_NAME=$EMAILS_FROM_NAME
ENV EMAILS_FROM_EMAIL=$EMAILS_FROM_EMAIL
ENV EMAILS_ENABLED=$EMAILS_ENABLED
ENV SMTP_HOST=$SMTP_HOST
ENV SMTP_PORT=$SMTP_PORT


# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Create Alembic folder and configuration
RUN alembic init alembic

# Apply Alembic migrations
RUN alembic upgrade head

# Run main.py when the container launches
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
