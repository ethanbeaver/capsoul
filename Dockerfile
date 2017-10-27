# Start with a Python image.
FROM python:latest

# Some stuff that everyone has been copy-pasting
# since the dawn of time.
ENV PYTHONUNBUFFERED 1

# Install some necessary things.
RUN apt-get update
RUN apt-get install -y libssl-dev 

# Copy all our files into the image.
RUN mkdir /code
WORKDIR /code
COPY . /code/

# Install our requirements.
RUN pip install -U pip
RUN pip install -Ur requirements.txt

#Create DB
RUN python /code/manage.py makemigrations
RUN python /code/manage.py migrate

EXPOSE 8000

# Specify the command to run when the image is run.
CMD python /code/manage.py runserver 8000
