FROM ubuntu:14.04

RUN apt-get update
RUN apt-get -y install python-dev python-pip && \
    pip install --upgrade pip==1.5.6

# Add all files in current directory to the container
ADD . /opt/python-flask
WORKDIR /opt/python-flask
RUN pip install -r requirements.txt


# Allow mounting an external folder here
VOLUME ["/opt/python-flask"]

ENTRYPOINT ["python", "server.py"]
