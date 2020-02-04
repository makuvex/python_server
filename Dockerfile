FROM ubuntu:18.04
FROM python:3.8

RUN apt-get update -y
RUN apt-get install nano
RUN apt-get install -y locales locales-all

ENV LC_ALL ko_KR.UTF-8
ENV LANG ko_KR.UTF-8
ENV LANG ko_KR.EUC-KR
ENV LANGUAGE ko_KR:ko:en_GB:en

COPY . /app
WORKDIR /app

RUN apt-get install -y python3-pip python-dev build-essential
RUN pip3 install flask
RUN pip3 install flask-restful
RUN pip3 install flask-mysql
RUN pip3 install PyMysql
RUN pip3 install requests

EXPOSE 5000

CMD ["python", "app.py"]

