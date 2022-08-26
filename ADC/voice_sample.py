import sounddevice as sd
import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile

duration = 3
fs = 10000
print("Recording ... ")
audio = sd.rec(int(duration*fs), samplerate=fs, channels=1, dtype=np.float32)
sd.wait()
print("Done ...")

t = np.arange(0, 3, 1/fs)
fx = np.fft.fftfreq(len(t), 1/fs)
audio_ft = np.fft.fft(audio)/len(t)

plt.plot(t, audio)

plt.figure()
plt.plot(fx, np.abs(audio_ft))

wavfile.write("ex_1.wav", fs, audio)
plt.show()




