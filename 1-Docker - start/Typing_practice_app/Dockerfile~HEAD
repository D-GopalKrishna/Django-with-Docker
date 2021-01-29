

#FROM python:3.7
#ENV PYTHONUNBUFFERED=1
#ENV PYTHONDONTWRITEBYTECODE 1
#
#WORKDIR /code
#ENV PYTHONPATH "${PYTHONPATH}:/control"
#COPY requirements.txt /code/
#RUN pip install -r requirements.txt
#COPY . /code/
#
#
#













# Pull Base Image
FROM python:3.7

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1


# Set work directory
WORKDIR / code

# Install dependencies
COPY Pipfile Pipfile.lock /code/
RUN pip install pipenv
#RUN pipenv install --system

# Copy project
COPY . /copy/

