# Name : Akhil Kushe
# Roll No: 191104003
# Class : TE, Sem V
# Branch : Electronics and Telecommunication Engg.
# Goa College of Engineering, Farmagudi
import numpy as np
import matplotlib.pyplot as plt

Vc = 2  #Carrier Amplitude
fc = 8  #Carrier Frequency
fs = 1000   #Sampling Frequency
t = np.arange(0, 5, 1/fs)   #Time series index
carrier = Vc*np.sin(2*np.pi*fc*t)   #Carrier signal
carrier_ft = np.fft.fft(carrier)/len(t)     #Carrier FFT
fb = fc/4       # Bit Rate
arr = np.array([0, 0, 1, 1, 1, 0, 1, 0, 0, 1]) # Bipolar NRZ Bit Patternz
#Generate bit pattern waveform
def squareGen(arr, t, fb):
    res = []
    tb = 1/fb
    for i in t:
        res.append(arr[int(i//tb)])
    return np.array(res)

b_t = squareGen(arr, t, fb)     # Modulating signal
b_t_ft = np.fft.fft(b_t)/len(t) # Modulating signal fourier transform
v_ook = b_t*carrier             # Modulated signal
v_ook_ft = np.fft.fft(v_ook)/len(t) # Modulated signal Fourier transform
fftx = np.fft.fftfreq(len(t), 1/fs) # Frequency indices
#Saving all the figures
def save_fig(x, y, title, x_label, y_label, x_lim):
    plt.figure(figsize=(10, 4))
    plt.plot(x, y)
    plt.xlim(x_lim)
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.savefig(title)
save_fig(t, b_t, "Modulating Signal", "time (sec)", "Amplitude (V)", (0, 5))
save_fig(t, carrier, "Carrier Signal", "time (sec)", "Amplitude (V)", (0, 3))
save_fig(t, v_ook, "Modulated Signal", "time(sec)", "Amplitude(V)", (0, 5))
save_fig(fftx, np.abs(b_t_ft), "Modulating signal fourier transform", "Frequencies(Hz)", "Magnitude", (-50, 50))
save_fig(fftx, np.abs(carrier_ft), "Carrier signal fourier transform", "Frequencies(Hz)", "Magnitude", (-50, 50))
save_fig(fftx, np.abs(v_ook_ft), "Modulated signal fourier transform", "Frequencies(Hz)", "Magnitude", (-50, 50))
