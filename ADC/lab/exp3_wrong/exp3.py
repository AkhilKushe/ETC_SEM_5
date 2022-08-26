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

fc1 = 20               # Carrier frequency
fc2 = 50

sampling_frequency = 500
# Time series for plotting
t = np.arange(start_time, finish_time, 1/sampling_frequency)                

signal1 = Vm1*np.cos(2*np.pi*fm1*t)                # Tone 1
signal2 = Vm2*np.cos(2*np.pi*fm2*t)                # Tone 2

#modulating_signal = signal1 + signal2              # Modulating signal m(t)

# x axis frequencies for fourier plot
frequencies = np.fft.fftfreq(len(t), 1/sampling_frequency)     
# Signal1 DFT             
s1_ft = np.fft.fft(signal1)/len(t) 
# Signal 2 DFT
s2_ft = np.fft.fft(signal2)/len(t)            

carrier1 = Vc*np.cos(2*np.pi*fc1*t)                 # Defining carrier signal
carrier2 = Vc*np.cos(2*np.pi*fc2*t)                 # Defining carrier signal
c1_ft = np.fft.fft(carrier1)/len(t)           # Carrier 1 signal dft
c2_ft = np.fft.fft(carrier2)/len(t)           # Carrier 2 signal dft

# defining modulated signal
sig1_mod = carrier1*signal1/Vc 
sig2_mod = carrier2*signal2/Vc

modulated_signal = sig1_mod + sig2_mod

# DFT of am signal                          
am_ft = np.fft.fft(modulated_signal)/len(modulated_signal)                  

def lpf_filter(fh, frequencies):
    lpf_freq = fh                                      # Low pass filter frequency
    lpf = []
    for xi in frequencies:                            # LPF filter DFT
        if np.abs(xi) <= lpf_freq:
            lpf.append(1)
        else:
            lpf.append(0)

    lpf = np.array(lpf)
    return lpf

def band_pass(fc, B, frequencies):
    bpf = []                                         # Band pass filter
    for xi in frequencies:                           
        if fc-(B/2) <= np.abs(xi) <= fc +(B/2):
            bpf.append(1)
        else:
            bpf.append(0)

    bpf = np.array(bpf)
    return bpf

def demodulator(fc, B, am_ft):
    am_s_ft = band_pass(fc, B, frequencies)*am_ft
    am_s = np.fft.ifft(am_s_ft)*len(t)

    carrier = np.cos(2*np.pi*fc*t)
    # Intermediate signal in synchronous detection
    intermediate_signal = am_s*carrier                           
    is_ft = np.fft.fft(intermediate_signal)/len(intermediate_signal)

    demod_ft = is_ft*2*lpf_filter(B/2, frequencies)                      # DFT of demodulated signal
    demod_signal = np.fft.ifft(demod_ft)*len(t)     # Demodulated signal

    return demod_signal


# Plotting and saving graphs
def save_fig(x, y, title, x_label, y_label, x_lim):
    plt.figure(figsize=(10, 4))
    plt.plot(x, y)
    plt.xlim(x_lim)
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.savefig(title)

dmod_1 = demodulator(fc1, 2*fm1 + 4, am_ft)
dmod_2 = demodulator(fc2, 2*fm2 + 4, am_ft)

save_fig(t, signal1, "Signal 1", "Time (sec)", "Amplitude (V)", (0, 5))
save_fig(t, signal2, "Signal 2", "Time (sec)", "Amplitude (V)", (0, 5))
save_fig(t, modulated_signal, "Modulated Signal", "Time (sec)", "Amplitude (V)", (0, 5))
save_fig(t, dmod_1, "Demodulated Signal 1", "Time (sec)", "Amplitude (V)", (0, 5))
save_fig(t, dmod_2, "Demodulated Signal 2", "Time (sec)", "Amplitude (V)", (0, 5))


save_fig(frequencies, np.abs(am_ft), "Modulated signal Fourier Transform", "Frequencies (Hz)", "Magnitude", (-80, 80))
save_fig(frequencies, np.abs(s1_ft), "Signal 1 Fourier Transform", "Frequencies (Hz)", "Magnitude", (-80, 80))
save_fig(frequencies, np.abs(s2_ft), "Signal 2 signal Fourier Transform", "Frequencies (Hz)", "Magnitude", (-80, 80))

bpf = band_pass(fc1, 2*fm1, frequencies)
save_fig(frequencies, np.abs(bpf), "BPF Fourier Transform", "Frequencies (Hz)", "Magnitude", (-80, 80))



