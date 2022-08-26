# Name : Akhil Kushe
# Roll No: 191104003
# Class : TE, Sem V
# Branch : Electronics and Telecommunication Engg.
# Goa College of Engineering, Farmagudi
import numpy as np
import matplotlib.pyplot as plt

Vm = 2      # Message signal amplitude
fm = 2      # Message signal Frequency
fs = 1000   # Sampling Frequency
t = np.arange(0, 3, 1/fs)   # Time indices
msg = Vm*np.sin(2*np.pi*fm*t)   # Message signal
msg_ft = np.fft.fft(msg)/len(t) # Message signal fourier transform
# Designing low pass filter
def lpf_filter(fh, frequencies):
    lpf_freq = fh        
    lpf = []
    for xi in frequencies:                         
        if np.abs(xi) <= lpf_freq:
            lpf.append(1)
        else:
            lpf.append(0)

    lpf = np.array(lpf)
    return lpf
# Designing quantizer
def quantizer(arr, Vl, Vh, N):
    M = 2**N
    s = (Vh-Vl)/M   # Step size
    mq = np.arange(Vl+s/2, Vh-s/2 + 0.1, s) #Bin values
    quantized = []  # Store quantized values
    encoded = []    # Store encoded values
    for i in arr:
        l = int(i//s)
        if l == len(mq):
            l = len(mq) -1       
        quantized.append(mq[l]) 
        encoded.append(bin(l))
    return np.array(quantized), np.array(encoded, dtype=np.str)
    
quantized, encoded = quantizer(msg+Vm, 0, 4, 2) #2 bit encoding from 0-4 V
#Designing decoder 
def decoder(arr,Vl, Vh, N):
    M = 2**N
    s = (Vh-Vl)/M
    mq = np.arange(Vl+s/2, Vh-s/2 + 0.1, s)
    d = np.array([int(i, 0) for i in arr])
    decoded = []
    for i in d:
        decoded.append(mq[i])
    return np.array(decoded)
print(encoded)
decoded = decoder(encoded, 0, 4, 2) # Decoded signal
reconstructed = decoded - Vm    # Reconstructed signal
reconstructed_fft = np.fft.fft(reconstructed)/len(t)    # Reconstructed signal fourier teransform
fftx = np.fft.fftfreq(len(t), 1/fs) # Frequency indices
lpf = lpf_filter(3, fftx)   #Low pass filter
v_m_recovered_ft = lpf*reconstructed_fft    # Recovered signal
v_m_recovered = np.fft.ifft(v_m_recovered_ft)*len(t)    #Recovered signal Fourier transform
# Saving all figures
def save_fig(x, y, title, x_label, y_label, x_lim, y2=None, y2_b=False):
    plt.figure(figsize=(10, 4))
    plt.plot(x, y)
    if y2_b:
        plt.plot(x, y2)
    plt.xlim(x_lim)
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    #plt.savefig(title)
save_fig(t, msg, "Message signal", "time(sec)", "Amplitude(v)", (0, 3))
save_fig(t, quantized, "Quantized signal", "time(sec)", "Amplitude(v)", (0, 3))
save_fig(t, reconstructed, "Reconstructed and signal", "time(sec)", "Amplitude(v)", (0, 3))
save_fig(t, v_m_recovered, "Recovered and origional signal", "time(sec)", "Amplitude(v)", (0, 3), y2=msg, y2_b=True)
save_fig(fftx, np.abs(msg_ft), "Message Signal Fourier Transform", "frequencies(Hz)", "Magnitude", (-20, 20))
save_fig(fftx, np.abs(reconstructed_fft), "Reconstructed Signal Fourier Transform", "frequencies(Hz)", "Magnitude", (-20, 20))
save_fig(fftx, np.abs(v_m_recovered_ft), "Recovered Signal Fourier Transform", "frequencies(Hz)", "Magnitude", (-20, 20))
