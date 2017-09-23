FROM whilgeek/start_image_python:latest
MAINTAINER Yang Liu <whilgeek@gmail.com>

ADD . /app
WORKDIR /app

RUN pip install --upgrade -r requirements.txt
