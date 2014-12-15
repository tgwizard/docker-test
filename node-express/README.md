# Docker and node express


## Using Docker


Build the image:

```bash
docker build --rm -t tgwizard/node-express .
```

Run in "development" mode (with autoreloading):

```bash
docker run -p 5000:5000 --env NODE_ENV=debug -v ${PWD}:/opt/node-express  tgwizard/node-express
```

Access site:

```bash
curl `boot2docker ip 2> /dev/null`:5000
open http://`boot2docker ip 2> /dev/null`:5000
```

Enter docker instance with bash:

```bash
# -i for interactive, keep STDIN open
# -t allocate a TTY
# -v to mount the current directory to /opt/node-express in the container
# --entrypoint to override what is in the Dockerfile
docker run -i -t -v ${PWD}:/opt/node-express --entrypoint=bash tgwizard/node-express
```

Update requirements:

```bash
# 1. Enter with bash
npm install --save[-dev] <package>
```
