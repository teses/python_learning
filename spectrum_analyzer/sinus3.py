"""
    https://realpython.com/python-scipy-fft/
"""

import numpy as np
from matplotlib import pyplot as plt
from scipy.fft import fft, fftfreq
from scipy.fft import rfft, rfftfreq

SAMPLE_RATE = 44100  # Hertz
DURATION = 2  # Seconds

def generate_sine_wave(freq, sample_rate, duration):
    x = np.linspace(0, duration, sample_rate * duration, endpoint=False)
    frequencies = x * freq
    # 2pi because np.sin takes radians
    y = np.sin((2 * np.pi) * frequencies)
    return x, y

# Generate tones and mixe together
_, nice_tone = generate_sine_wave(400, SAMPLE_RATE, DURATION)
_, noise_tone = generate_sine_wave(4000, SAMPLE_RATE, DURATION)
noise_tone = noise_tone * 0.3
mixed_tone = nice_tone + noise_tone

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


# plot first 400
plt.plot(xf, np.abs(yf))
#plt.plot(normalized_tone[:400])
plt.show()




