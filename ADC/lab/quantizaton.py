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
t = np.arange(0, 7, 1/fs)   # Time indices
msg = t
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
    print(s)
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
    
quantized, encoded = quantizer(msg, 0, 8, 3) #2 bit encoding from 0-4 V
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

plt.figure(figsize=(10, 4))
plt.plot(t, msg, label="Message signal")
plt.plot(t, quantized, label="Quantized signal")
plt.figure(figsize=(10, 4))
error = msg - quantized
plt.plot(t, error)

mse = np.mean(error*error)

print(mse)

plt.show()