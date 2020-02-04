FROM python:3.7.1
ENV PYTHONUNBUFFERED 1
RUN mkdir /docker_api
WORKDIR /docker_api
COPY requirements.txt .
RUN pip install -r requirements.txt
