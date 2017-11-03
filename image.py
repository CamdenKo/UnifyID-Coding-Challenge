from PIL import Image

from requester import request_to_random

def create_image(width, height):
  return Image.new('RGB', (width, height), 'black')

def set_pixels(img, rgb_arr, cluster_size):
  pixels = img.load()
  counter = 0
  col = 0
  row = 0
  while col < img.size[0]:
    row = 0
    while row < img.size[1]:
      vals = (rgb_arr[counter], rgb_arr[counter + 1], rgb_arr[counter + 2])
      set_cluster(vals, pixels, col, col + cluster_size - 1, row, row + cluster_size - 1)
      row += cluster_size
      counter = counter + 3
    col += cluster_size

def set_cluster(vals, pixels, min_x, max_x, min_y, max_y):
  x = min_x
  y = min_y
  while x <= max_x:
    y = min_y
    while y <= max_y:
      pixels[x, y] = vals
      y += 1
    x += 1

def create_random_image(file_name):
  width = 128
  height = 128
  cluster_size = 8
  rgb_arr = request_to_random((width * height * 3) / cluster_size, 0, 255)
  img = create_image(width, height)
  set_pixels(img, rgb_arr, cluster_size)
  img.show()
  img.save(file_name, 'BMP')

