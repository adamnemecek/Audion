import wave, struct
import numpy as np
CHUNK = 4096


def load_wav_file(name):
  f = wave.open(name, "rb")
  chunk = []
  #read CHUNK number of frames from the data
  data0 = f.readframes(CHUNK)
  while data0 != '':  # f.getnframes()
  	# data=np.fromstring(data0, dtype='float32')
    # data = np.fromstring(data0, dtype='uint16')
    data = np.fromstring(data0, dtype='uint8')
    data = (data + 128) / 255.  # 0-1 for Better convergence
    # chunks.append(data)
    print data
    chunk.extend(data)
    data0 = f.readframes(CHUNK)
  # finally trim:
  chunk = chunk[0:CHUNK * 2]  # should be enough for now -> cut
  chunk.extend(np.zeros(CHUNK * 2 - len(chunk)))  # fill with padding 0's
  return chunk
