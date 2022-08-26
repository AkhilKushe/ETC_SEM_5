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

fm1 = 2               # Signal 1 frequency
fm2 = 5               # Signal 2 frequency

sampling_frequency = 500
# Time series for plotting
t = np.arange(start_time, finish_time, 1/sampling_frequency)                

signal1 = Vm1*np.cos(2*np.pi*fm1*t)                # Tone 1
signal2 = Vm2*np.cos(2*np.pi*fm2*t)                # Tone 2

# x axis frequencies for fourier plot
frequencies = np.fft.fftfreq(len(t), 1/sampling_frequency)     
# Signal1 DFT             
s1_ft = np.fft.fft(signal1)/len(t) 
# Signal 2 DFT
s2_ft = np.fft.fft(signal2)/len(t)            

# Multiplexed signal
multiplexed_sig = signal1 + signal2                         
# Multiplexed signal fft
multiplexed_fft = np.fft.fft(multiplexed_sig)/len(t)    

# Band pass filter
def band_pass(fc, B, frequencies):
    bpf = []                                         
    for xi in frequencies:                           
        if fc-(B/2) <= np.abs(xi) <= fc +(B/2):
            bpf.append(1)
        else:
            bpf.append(0)

    bpf = np.array(bpf)
    return bpf

# Demultiplexer
def demux(fc, B, mux_sig_ft):                        
    demux_ft = band_pass(fc, B, frequencies)*mux_sig_ft
    demux_sig = np.fft.ifft(demux_ft)*len(t)

    return demux_sig, demux_ft

# Plotting and saving graphs
def save_fig(x, y, title, x_label, y_label, x_lim):
    plt.figure(figsize=(10, 4))
    plt.plot(x, y)
    plt.xlim(x_lim)
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.savefig(title)

# Extracting signal 1
demux_sig_1, demux_sig_1_ft = demux(fm1, 2, multiplexed_fft)
# Extracting singal 2
demux_sig_2, demux_sig_2_ft = demux(fm2, 2, multiplexed_fft)

#Plot and Save all graphs
save_fig(t, signal1, "Signal 1", "Time (sec)", "Amplitude (V)", (0, 5))
save_fig(t, signal2, "Signal 2", "Time (sec)", "Amplitude (V)", (0, 5))
save_fig(t, multiplexed_sig, "Multiplexed signal", "Time (sec)", "Amplitude (V)", (0, 5))
save_fig(t, demux_sig_1, "Demultiplexed Signal 1", "Time (sec)", "Amplitude (V)", (0, 5))
save_fig(t, demux_sig_2, "Demultiplex,ed Signal 2", "Time (sec)", "Amplitude (V)", (0, 5))
save_fig(frequencies, np.abs(multiplexed_fft), "Multiplexed signal Fourier Transform", "Frequencies (Hz)", "Magnitude", (-40, 40))
save_fig(frequencies, np.abs(s1_ft), "Signal 1 Fourier Transform", "Frequencies (Hz)", "Magnitude", (-40, 40))
save_fig(frequencies, np.abs(s2_ft), "Signal 2 signal Fourier Transform", "Frequencies (Hz)", "Magnitude", (-40, 40))
save_fig(frequencies, np.abs(demux_sig_1_ft), "Demultiplexed Signal 1 signal Fourier Transform", "Frequencies (Hz)", "Magnitude", (-40, 40))
save_fig(frequencies, np.abs(demux_sig_2_ft), "Demultiplexed Signal 2 signal Fourier Transform", "Frequencies (Hz)", "Magnitude", (-40, 40))

