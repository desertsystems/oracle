# docker pipline for python flask server
FROM ubuntu:bionic
COPY . /app
WORKDIR /app
RUN apt-get update
RUN apt-get install -y python3 python3-dev python3-pip
RUN pip3 install flask
ENTRYPOINT [ "python3" ]
CMD ["app.py"]