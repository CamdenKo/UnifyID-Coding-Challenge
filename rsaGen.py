from crypto.PublicKey import RSA

from requester import request_to_random

def generate_e(lower_bound, upper_bound):
  request_to_random(1, lower_bound, upper_bound)

def create_rsa(file_name):
  file = open(file_name, 'w')
  key = RSA.generate(2048, e=65537)
  file.write(key.exportKey('PEM'))
  file.close()




