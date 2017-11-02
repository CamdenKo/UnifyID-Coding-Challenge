# NOTE: For this coding exercise I will simply store the 3 seconds sound in memory, if ti were longer I would stream this from disk.

import wave
import struct
from requester import request_to_random

def create_wav_file(file_name):
  return wave.Wave_write(file_name)

def create_sounds_arr(sample_rate, duration):
  num_samples = int(duration * sample_rate / 1000.0)
  return request_to_random(num_samples, -32767, 32767)

def save_wav(sounds_arr, wav_file, sample_rate):
  nchannels = 1
  sampwidth = 2
  nframes = len(sounds_arr)
  comptype = 'NONE'
  compname = 'not compressed'
  wav_file.setparams((nchannels, sampwidth, sample_rate, nframes, comptype, compname))

  for sample in sounds_arr:
    wav_file.writeframes(struct.pack('h', sample))

  wav_file.close()

def create_random_wav(file_name):
  sample_rate = 44100.0
  duration = 30 #MS
  sounds_arr = create_sounds_arr(sample_rate, duration)
  wav_file = create_wav_file(file_name)
  save_wav(sounds_arr, wav_file, sample_rate)

# save_file('as')
