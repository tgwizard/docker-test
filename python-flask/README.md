# Docker and python flask

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
docker run -p 5000:5000 --env DEBUG=1 -v ${PWD}:/opt/python-flask --entrypoint=python tgwizard/python-flask server.py
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
# -v to mount the current directory to /opt/python-flask in the container
# --entrypoint to override what is in the Dockerfile
docker run -i -t -v ${PWD}:/opt/python-flask --entrypoint=bash tgwizard/python-flask
```

Update requirements:

```bash
# 1. Enter with bash
pip install <package>
pip freeze > requirements.txt
```

Run spam client:

```bash
docker run -i -t -v ${PWD}:/opt/python-flask --entrypoint=python tgwizard/python-flask spam-client.py http://`boot2docker ip 2> /dev/null`:5000
```
