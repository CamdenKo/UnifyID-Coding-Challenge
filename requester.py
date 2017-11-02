import secrets
from jsonrpcclient.http_client import HTTPClient

client = HTTPClient('https://api.random.org/json-rpc/1/invoke')
def request_to_random(n, minRGB, maxRGB):
  response = client.request('generateIntegers', apiKey=secrets.randomAPI, n=n, min=minRGB, max=maxRGB)
  return response['random']['data']
