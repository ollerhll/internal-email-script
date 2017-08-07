FROM python:2.7.13

ADD . /code
WORKDIR /code

RUN ["python", "mailSend.py"]

