import secrets
from jsonrpcclient.http_client import HTTPClient

client = HTTPClient('https://api.random.org/json-rpc/1/invoke')
def request_to_random(n, min_val, max_val):
  response = client.request('generateIntegers', apiKey=secrets.randomAPI, n=n, min=min_val, max=max_val)
  return response['random']['data']
