# Name : Akhil Kushe
# Roll No: 191104003
# Class : TE, Sem V
# Branch : Electronics and Telecommunication Engg.
# Goa College of Engineering, Farmagudi

import matplotlib.pyplot as plt
import numpy as np

start_time = 0
finish_time = 5

Vm1 = 3               # Signal 1 amplitude
Vm2 = 2               # Signal 2 amplitude

Vc = 8                # Carrier signal amplitude

fm1 = 2               # Signal 1 frequency
fm2 = 5               # Signal 2 frequency

fc = 50               # Carrier frequency

sampling_frequency = 200
# Time series for plotting
t = np.arange(start_time, finish_time, 1/sampling_frequency)                

signal1 = Vm1*np.cos(2*np.pi*fm1*t)                # Tone 1
signal2 = Vm2*np.cos(2*np.pi*fm2*t)                # Tone 2

modulating_signal = signal1 + signal2              # Modulating signal m(t)

# x axis frequencies for fourier plot
frequencies = np.fft.fftfreq(len(t), 1/sampling_frequency)     
# Modulating signal DFT             
ms_ft = np.fft.fft(modulating_signal)/len(modulating_signal)                

carrier = Vc*np.cos(2*np.pi*fc*t)                 # Defining carrier signal
c_ft = np.fft.fft(carrier)/len(carrier)           # Carrier signal dft

# defining modulated signal
modulated_signal = carrier*modulating_signal/Vc   
# DFT of am signal                          
am_ft = np.fft.fft(modulated_signal)/len(modulated_signal)                  

lpf_freq = 6                                      # Low pass filter frequency
lpf = []
for xi in frequencies:                            # LPF filter DFT
    if np.abs(xi) <= lpf_freq:
        lpf.append(1)
    else:
        lpf.append(0)

lpf = np.array(lpf)

# Intermediate signal in synchronous detection
intermediate_signal = modulated_signal*carrier/Vc                           
is_ft = np.fft.fft(intermediate_signal)/len(intermediate_signal)

demod_ft = is_ft*2*lpf                          # DFT of demodulated signal
demod_signal = np.fft.ifft(demod_ft)*len(t)     # Demodulated signal


# Plotting and saving graphs
def save_fig(x, y, title, x_label, y_label, x_lim):
    plt.figure(figsize=(10, 4))
    plt.plot(x, y)
    plt.xlim(x_lim)
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.savefig(title)

save_fig(t, modulating_signal, "Modulating Signal", "Time (sec)", "Amplitude (V)", (0, 5))
save_fig(t, carrier, "Carrier Signal", "Time (sec)", "Amplitude (V)", (0, 5))
save_fig(t, modulated_signal, "Modulated Signal", "Time (sec)", "Amplitude (V)", (0, 5))
save_fig(t, demod_signal, "Demodulated Signal", "Time (sec)", "Amplitude (V)", (0, 5))

save_fig(frequencies, np.abs(ms_ft), "Modulating signal Fourier Transform", "Frequencies (Hz)", "Magnitude", (-80, 80))
save_fig(frequencies, np.abs(c_ft), "Carier signal Fourier Transform", "Frequencies (Hz)", "Magnitude", (-80, 80))
save_fig(frequencies, np.abs(am_ft), "Modulated signal Fourier Transform", "Frequencies (Hz)", "Magnitude", (-80, 80))
save_fig(frequencies, np.abs(demod_ft), "Demodulated signal Fourier Transform", "Frequencies (Hz)", "Magnitude", (-80, 80))

save_fig(frequencies, lpf, "Lowpass filter Fourier Transform", "Frequencies (Hz)", "Magnitude", (-80, 80))







