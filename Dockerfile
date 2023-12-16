# Use an official Python runtime as a parent image
FROM python:3.9.6-slim

# set a directory for the app
WORKDIR /usr/src/app

# copy all the files to the container
COPY . .

# install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# define the port number the container should expose
EXPOSE 8000

# Define environment variable
ENV DATABASE_URI=$DATABASE_URI
ENV SECRET_KEY=$SECRET_KEY
ENV ALGORITHM=$ALGORITHM
ENV ACCESS_TOKEN_EXPIRE_MINUTES=$ACCESS_TOKEN_EXPIRE_MINUTES
SMTP_HOST=$SMTP_HOST
SMTP_PORT=$SMTP_PORT
SMTP_LOGIN=$SMTP_LOGIN
SMTP_PASSWORD=$SMTP_PASSWORD
SMTP_API_KEY=$SMTP_API_KEY
EMAILS_ENABLED=$EMAILS_ENABLED
EMAILS_FROM_NAME=$EMAILS_FROM_NAME
EMAILS_FROM_EMAIL=$EMAILS_FROM_EMAIL
WEBSITE_DOMAIN=$WEBSITE_DOMAIN


CMD ["python", "./main.py"]