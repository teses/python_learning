import pyaudio
import struct
import numpy as np
import matplotlib.pyplot as plt




CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100

p = pyaudio.PyAudio()
stream = p.open(
    format = FORMAT,
    channels = CHANNELS,
    rate = RATE,
    input = True,
    output = False,
    frames_per_buffer = CHUNK,
    start = True
    )

fig, ax = plt.subplots()
x = np.arange(0, 2 * CHUNK, 2)
line, = ax.plot(x, np.random.rand(CHUNK))

ax.set_ylim(0, 255)
ax.set_xlim(0, CHUNK)
plt.show(block=False)

while True:
    data = stream.read(CHUNK)
    data_int = np.array(struct.unpack(str(CHUNK*2) + 'B', data), dtype='b')[::2] + 128
    line.set_ydata(data_int)
    fig.canvas.draw()
    fig.canvas.flush_events()

