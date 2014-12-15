import sys
import thread
import requests


address = sys.argv[1]

def make_request():
    print requests.get(address).text
