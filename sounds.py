# NOTE: For this coding exercise I will simply store the 3 seconds sound in memory, if ti were longer I would stream this from disk.

import wave
from requester import request_to_random

def create_wav_file(file_name):
  return wave.Wave_write(file_name)

def create_sounds_arr(sample_rate, duration):
  num_samples = duration * sample_rate / 1000.0
  return request_to_random(num_samples, )

def create_random_wav():
  sample_rate = 44100.0
  duration = 3000 #MS
  audio = create_sounds(sample_rate, duration)
# save_file('as')
