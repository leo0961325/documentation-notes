FROM centos/python-36-centos7
LABEL Author="cool21540125@gmail.com"
COPY ./app/ /app
WORKDIR /app
RUN pip install -r requirements.txt
CMD ["python", "manage.py"]
