# Docker and python flask

## Docker

Install Docker: https://docs.docker.com/installation/

For Mac OS X, also setup the current shell:

```bash
boot2docker shellinit
# Execut the echoed export commands
```

And find the IP of the Docker container:

```bash
boot2docker ip
```


## Using Docker


Build the image:

```bash
docker build --rm -t tgwizard/python-flask .
```

Run in "production" mode:

```bash
docker run -p 5000:5000 tgwizard/python-flask
```

Run in "development" mode (with autoreloading):

```bash
docker run -p 5000:5000 --env DEBUG=1 -v ${PWD}:/opt/python-flask tgwizard/python-flask
```

curl:

```bash
curl `boot2docker ip 2> /dev/null`:5000
```

Enter docker instance with bash:

```bash
# -i for interactive, keep STDIN open
# -t allocate a TTY
# -v to mount the current directory to /opt/python-flask in the container
# --entrypoint to override what is in the Dockerfile
docker run -i -t -v ${PWD}:/opt/python-flask --entrypoint=/bin/bash tgwizard/python-flask
```

Update requirements:

```bash
# 1. Enter with bash
pip install <package>
pip freeze > requirements.txt
```
