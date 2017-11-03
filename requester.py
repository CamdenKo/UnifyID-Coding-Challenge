"""Requester for Random.org API, must save Random.org API key as randomAPI in secrets.py"""

import secrets
from jsonrpcclient.http_client import HTTPClient

client = HTTPClient('https://api.random.org/json-rpc/1/invoke')
def request_to_random(n, min_val, max_val):
  """n - the number of numbers (int), min_val (int), max_val (int), returns an array of ints with count n, [min_val, max_val]"""
  response = client.request('generateIntegers', apiKey=secrets.randomAPI, n=n, min=min_val, max=max_val)
  return response['random']['data']
