FROM ubuntu:14.04

RUN apt-get update
RUN apt-get -y install curl && \
    curl -sL https://deb.nodesource.com/setup | sudo bash -
RUN apt-get -y install build-essential && \
    apt-get -y install nodejs && \
    apt-get -y install ruby && \
    gem install foreman

# Add package.json by itself so we don't have to reinstall
# npm requirements when we rebuild the image because some files
# have changed.
ADD ./package.json /opt/node-express/package.json
WORKDIR /opt/node-express

RUN npm install

# Add all files in current directory to the container
ADD . /opt/node-express

# Allow mounting an external folder here
VOLUME ["/opt/node-express"]

ENTRYPOINT ["node", "app.js"]
