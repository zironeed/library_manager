FROM python:3.10-slim-bullseye

WORKDIR /library_manager

COPY ./requirements.txt /library_manager/

RUN pip install --upgrade pip
RUN apt-get update && \
      apt-get -y install sudo
RUN apt-get update && sudo apt-get install -y gcc
RUN sudo apt-get install -y python3-dev default-libmysqlclient-dev
RUN pip install -r requirements.txt

COPY ./library_manager /library_manager/
