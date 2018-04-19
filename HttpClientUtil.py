import requests
import json
import logging
import sys

class HttpClientUtil:
    def __init__(self):
        FORMAT = '%(asctime)-15s %(clientip)s %(user)-8s %(message)s'
        logging.basicConfig(format=FORMAT)
    def call(self,Url,params):
        for k,v in params:
            