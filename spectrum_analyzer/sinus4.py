"""
    https://realpython.com/python-scipy-fft/
"""

import numpy as np
from matplotlib import pyplot as plt
from scipy.fft import fft, fftfreq
from scipy.fft import rfft, rfftfreq

SAMPLE_RATE = 44100  # Hertz
DURATION = 4  # Seconds
EQ_CHUNKS = 10 # Equilizer Frequenz unterteilung


def generate_sine_wave(freq, sample_rate, duration):
    x = np.linspace(0, duration, sample_rate * duration, endpoint=False)
    frequencies = x * freq
    # 2pi because np.sin takes radians
    y = np.sin((2 * np.pi) * frequencies)
    return x, y

###########################################################################
# Generate tones and mixe together
_, nice_tone = generate_sine_wave(1000, SAMPLE_RATE, DURATION)
_, noise_tone = generate_sine_wave(4000, SAMPLE_RATE, DURATION)
_, high_tone = generate_sine_wave(10000, SAMPLE_RATE, DURATION)
_, high_tone2 = generate_sine_wave(15000, SAMPLE_RATE, DURATION)
noise_tone = noise_tone * 0.3
mixed_tone = nice_tone + noise_tone + high_tone + high_tone2

# normalized bettween 16 Bit integer
normalized_tone = np.int16((mixed_tone / mixed_tone.max()) * 32767)

# Number of samples in normalized_tone
N = SAMPLE_RATE * DURATION

# fft
#yf = fft(normalized_tone)
#xf = fftfreq(N, 1 / SAMPLE_RATE)
# Note the extra 'r' at the front
yf = rfft(normalized_tone)
xf = rfftfreq(N, 1 / SAMPLE_RATE)
for x in xf:
    print(x)


###############################################################################################
## Chunks
# Calculate BINS (one way, there are others):
# https://stackoverflow.com/questions/29391815/sum-slices-of-consecutive-values-in-a-numpy-array
yfa = np.absolute(yf)
#yfa[0:8] = yfa[0:8]/20
sampleChunkSize = int(SAMPLE_RATE / (EQ_CHUNKS - 2))
BINS = [sum(yfa[current: current+sampleChunkSize]) for current in range(0, len(yfa), sampleChunkSize)]
# Convert to numpy array:
BINS = np.array(BINS)

# Normalize and round up to values between 0-10
BINS = np.interp(BINS, (BINS.min(), BINS.max()), (0, 10))
BINS = np.round(BINS)

for x in BINS:
    print(x)



# plot first 400
print(len(xf))
print(len(np.abs(yf)))
plt.plot(xf, np.abs(yf))
#plt.plot(normalized_tone[:400])
plt.show()




