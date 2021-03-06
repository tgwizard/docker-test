import os

import requests
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/crash')
def crash():
    return 1 // 0

@app.route('/test-perf')
def test_perf():
    requests.get('http://dn.se')
    requests.get('http://google.se')
    return 'ok'

if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=5000,
        debug=os.environ.get('DEBUG', False))
