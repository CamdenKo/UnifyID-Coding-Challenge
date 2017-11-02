import requests
import secrets
import json
import os
from PIL import Image
# from PIL import RGB
from jsonrpcclient.http_client import HTTPClient

client = HTTPClient('https://api.random.org/json-rpc/1/invoke')
def request_to_random(n, min, max):
  response = client.request('generateIntegers', apiKey=secrets.randomAPI, n=n, min=min, max=max)
  return response['random']['data']

def create_image(width, height):
  return Image.new('RGB', (width, height), 'black')

def set_pixels(img, rgb_arr):
  counter = 0
  pixels = img.load()
  for col in range(img.size[0]):
    for row in range(img.size[1]):
      pixels[col, row] = (rgb_arr[counter], rgb_arr[counter + 1], rgb_arr[counter + 2])
      counter = counter + 3

def create_random_image():
  width = 10 #128
  height = 10
  rgb_arr = request_to_random(width * height * 3, 0, 255)
  img = create_image(width, height)
  set_pixels(img, rgb_arr)
  img.show()
  img.save('randomImg', 'PNG')

create_random_image()
