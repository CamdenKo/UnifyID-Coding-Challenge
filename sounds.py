# NOTE: For this coding exercise I will simply store the 3 seconds sound in memory, if ti were longer I would stream this from disk.

import wave

audio = []
sample_rate = 44100.0

def save_file(file_name):
  wave.open('audio')

# save_file('as')
wave.Wave_write('audio')
