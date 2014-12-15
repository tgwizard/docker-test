FROM ubuntu:14.04

RUN apt-get update
RUN apt-get -y install python-dev python-pip && \
    pip install --upgrade pip==1.5.6 && \
    apt-get -y install ruby && \
    gem install foreman

# Add requirements.txt by itself so we don't have to reinstall
# pip requirements when we rebuild the image because some files
# have changed.
ADD ./requirements.txt /opt/python-flask/requirements.txt
WORKDIR /opt/python-flask

RUN pip install -r requirements.txt

# Add all files in current directory to the container
ADD . /opt/python-flask

# Allow mounting an external folder here
VOLUME ["/opt/python-flask"]

ENTRYPOINT ["foreman", "start", "--color"]
