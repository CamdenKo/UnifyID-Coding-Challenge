"""Resources needed to create a random 3s wav sound"""

# NOTE: For this coding exercise I will simply store the 3 seconds sound in memory, if ti were longer I would stream this from disk.

import wave
import struct
from requester import request_to_random

def create_wav_file(file_name):
  """Takes in a string (file_name) and returns a Wave.openFile instance"""
  return wave.Wave_write(file_name)

def create_sounds_arr(sample_rate, duration, sound_length):
  """Takes in sample_rate (int), duration (int), sound_length (int) and returns an array of sounds from -32767 to 32767"""
  num_samples = int(duration * sample_rate / sound_length / 1000.0)
  return request_to_random(num_samples, -32767, 32767)

def save_wav(sounds_arr, wav_file, sample_rate, sound_length):
  """Takes in sounds_arr (array of ints), wav_file (Wave.openFile instance), sample_rate (int), sound_length(int). Saves the wav_file and closes it"""
  nchannels = 1
  sampwidth = 2
  nframes = len(sounds_arr)
  comptype = 'NONE'
  compname = 'not compressed'
  wav_file.setparams((nchannels, sampwidth, sample_rate, nframes, comptype, compname))

  for sample in sounds_arr:
    for _ in range(sound_length):
      wav_file.writeframes(struct.pack('h', sample))

  wav_file.close()

def create_random_wav(file_name):
  """takes in a file_name and will save the random wav file to the file name"""
  sample_rate = 44100.0
  sound_length = 50
  duration = 3000 #MS
  sounds_arr = create_sounds_arr(sample_rate, duration, sound_length)
  wav_file = create_wav_file(file_name)
  save_wav(sounds_arr, wav_file, sample_rate, sound_length)

