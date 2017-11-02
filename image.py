from PIL import Image

from requester import request_to_random

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
  img.save('randomImg.bmp', 'BMP')

