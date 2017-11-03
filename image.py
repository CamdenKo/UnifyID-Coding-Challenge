"""Resources needed to create a random 128 * 128 BMP"""

from PIL import Image

from requester import request_to_random

def create_image(width, height):
  """width(int), height(int), returns an instance of Image"""
  return Image.new('RGB', (width, height), 'black')

def set_pixels(img, rgb_arr, cluster_size):
  """img(Image instance), rgb_arr(array of ints, each one being r,g, or b), cluster_size(int) sets all the pixels of the image according to rgb_arr with each rgb taking up cluster_size x cluster_size"""
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
  """vals(tuple of ints representing RGB), pixels(pixels property of Image instance), min_x(int), max_x(int), min_y(int), max_y(int) sets cluster covered by min to max x to y to the vals set"""
  x = min_x
  y = min_y
  while x <= max_x:
    y = min_y
    while y <= max_y:
      pixels[x, y] = vals
      y += 1
    x += 1

def create_random_image(file_name):
  """takes in a file_name(string) and saves a random bitmap to the file name"""
  width = 128
  height = 128
  cluster_size = 8
  rgb_arr = request_to_random((width * height * 3) / cluster_size, 0, 255)
  img = create_image(width, height)
  set_pixels(img, rgb_arr, cluster_size)
  img.show()
  img.save(file_name, 'BMP')

