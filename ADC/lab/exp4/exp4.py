# Name : Akhil Kushe
# Roll No: 191104003
# Class : TE, Sem V
# Branch : Electronics and Telecommunication Engg.
# Goa College of Engineering, Farmagudi

import matplotlib.pyplot as plt
import numpy as np

start_time = 0
finish_time = 5

Vm = 3                # Signal 1 amplitude
Vc = 8                # Carrier signal amplitude
fm = 2                # Signal 1 frequency
fc = 20               # Carrier frequency

sampling_frequency = 300
# Time series for plotting
t = np.arange(start_time, finish_time, 1/sampling_frequency)                
 
modulating_signal = -Vm*np.sin(2*np.pi*fm*t)  

# x axis frequencies for fourier plot
frequencies = np.fft.fftfreq(len(t), 1/sampling_frequency)     
# Modulating signal DFT             
ms_ft = np.fft.fft(modulating_signal)/len(modulating_signal)                

carrier = Vc*np.cos(2*np.pi*fc*t)
c_ft = np.fft.fft(carrier)/len(t)

def modulator(m):
    k = m*fm/Vm
    modulated_signal = Vc*np.cos(2*np.pi*fc*t + m*np.cos(2*np.pi*fm*t))
    am_ft = np.fft.fft(modulated_signal)/len(t)
    return k, m, modulated_signal, am_ft

k1, m1, mod1, mod1_ft = modulator(1)            #Modulating with m=1
k2, m2, mod2, mod2_ft = modulator(2.4)          #Modulating with k=2.4
k3, m3, mod3, mod3_ft = modulator(4)            #Modulating with k=4

# Plotting and saving graphs
def save_fig(x, y, title, x_label, y_label, x_lim, m=0, k=0):
    plt.figure(figsize=(10, 4))
    plt.plot(x, y)
    
    if k and m:
        plt.text(60, 1.2, "kf = %.2f"%k)
        plt.text(60, 1.1, "m = %.2f"%m)

    plt.xlim(x_lim)
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.savefig(title)

save_fig(t, mod3, "Modulated Signal", "Time (sec)", "Amplitude (V)", (0, 3))
save_fig(frequencies, np.abs(mod1_ft), "Modulated Signal 1 Fourier Transform", "Frequencies (Hz)", "Magnitude", (-80, 80), m1, k1)
save_fig(frequencies, np.abs(mod2_ft), "Modulated Signal 2 Fourier Transform", "Frequencies (Hz)", "Magnitude", (-80, 80), m2, k2)
save_fig(frequencies, np.abs(mod3_ft), "Modulated Signal 3 Fourier Transform", "Frequencies (Hz)", "Magnitude", (-80, 80), m3, k3)
