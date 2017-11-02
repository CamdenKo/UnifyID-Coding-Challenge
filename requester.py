import secrets
import json
from PIL import Image
from jsonrpcclient.http_client import HTTPClient

client = HTTPClient('https://api.random.org/json-rpc/1/invoke')
def request_to_random(n, min, max):
  response = client.request('generateIntegers', apiKey=secrets.randomAPI, n=n, min=min, max=max)
  return response['random']['data']
