FROM python:3.10-slim-bullseye

WORKDIR /library_manager

COPY ./requirements.txt /library_manager/

RUN pip install --upgrade pip
RUN apt-get update && apt-get install -y pkg-config
RUN pip install -r requirements.txt

COPY ./library_manager /library_manager/
