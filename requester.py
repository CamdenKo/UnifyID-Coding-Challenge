import requests
import secrets
import json
from PIL import Image
# from PIL import RGB
from jsonrpcclient.http_client import HTTPClient

client = HTTPClient('https://api.random.org/json-rpc/1/invoke')
def request_to_random(n, min, max):
  response = client.request('generateIntegers', apiKey=secrets.randomAPI, n=n, min=min, max=max)
  return response['random']['data']

def create_image(width, height):
  img = Image.new('RGB', (width, height), 'black')
  pixels = img.load()
  for col in range(img.size[0]):
    for row in range(img.size[1]):
      pixels[col, row] = (255, 0, 0)
  img.show()
create_image(100, 100)
