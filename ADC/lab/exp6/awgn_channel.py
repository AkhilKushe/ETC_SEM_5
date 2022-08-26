# Name : Akhil Kushe
# Roll No: 191104003
# Class : TE, Sem V
# Branch : Electronics and Telecommunication Engg.
# Goa College of Engineering, Farmagudi

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt1
import matplotlib.pyplot as plt2
import matplotlib.pyplot as plt3
import matplotlib.pyplot as plt4
import matplotlib.pyplot as plt5
import matplotlib.pyplot as plt6
import sys
from rtlsdr import RtlSdr
import numpy as np
from numpy import *
from scipy.fftpack import fftshift

def fft_shift(x):
    fft_output_shift = np.array([])
    P = len(x)
    for m in range(int(P/2)):
        fft_output_shift = np.append(fft_output_shift,x[int(m+P/2)])

    for m in range(int(P/2)):
        fft_output_shift = np.append(fft_output_shift,x[m])
    return fft_output_shift

def avgPS( x, N, fs):
    M = len(x)//N
    x_ = np.reshape(x[:M*N],(M,N)) * np.hamming(N)[None,:]
    X = np.fft.fftshift(np.fft.fft(x_,axis=1),axes=1)
    return r_[-N/2.0:N/2.0]/N*fs, mean(abs(X**2),axis=0)
######## Reading samples #############
fc = 900 #sys.argv[1] # Carrier frequency 
fc = float(fc)*1000000
sdr = RtlSdr()
print('\nCapturing samples at frequency: '+ str(fc/1e6)+ 'MHz')
sdr.sample_rate = sample_rate = 2400000 # Sampling rate
sdr.center_freq = fc
sdr.gain = 0
iq_samples = sdr.read_samples(8*2560) # Reading samples
sdr.close()  
del(sdr)
print("Processing the samples ...")
iq_samples=iq_samples[2000:] # Neglecting first 2000 samples
######## Plotting received signal amplitude #############
sam = 2500
y = range(1,sam)
y = [i/sample_rate/1e-3 for i in y]
plt1.plot(y,iq_samples[1:sam].real)
plt1.xlabel('Time (ms)')
plt1.ylabel('Received signal amplitude')
plt1.grid()
plt1.savefig("Exp1_receiver_noise" + ".png", bbox_inches='tight', pad_inches=0.5)
plt1.close()
######## Plotting PDF of Normal distribution #############
plt2.hist(iq_samples.real, density=True, linewidth=3,alpha=1, bins=70, label='Measured') # PDF of received samples
plt2.xlabel('Received signal amplitude')
plt2.ylabel('PDF')
x = np.linspace(-1.5,1.5,1000)
mu = 0
sig = np.std(iq_samples.real)
normal_pdf = [1/(sig*np.sqrt(2*np.pi))*np.exp(-(i-mu)**2/(2*sig**2)) for i in x]
plt2.plot(x, normal_pdf, 'r-', lw=2, label='Analytical')
plt2.grid()
plt2.legend()
plt2.savefig("Exp1_awgn_PDF" + ".png", bbox_inches='tight', pad_inches=0.5)
plt2.close()
f6 = plt6.figure(6)
# compute average power spectrum
f, sp = avgPS(iq_samples.real,N=1024,fs=sample_rate)
plt6.plot((f+fc)/1e6,10*log10(sp))
plt6.title('Average power spectrum')
plt6.xlabel('Frequency [MHz]')
plt6.grid()
plt6.savefig("Exp1_awgn_spectrum" + ".png", bbox_inches='tight', pad_inches=0.5)
plt6.close()
######## Plotting Autocorrelation function #############
samp = 500
corr = np.correlate(iq_samples[1:samp].real,iq_samples[1:samp].real,"full") # Autocorrelation of received signal 
plt3.plot(np.linspace(-samp/sample_rate/1e-3,samp/sample_rate/1e-3,len(corr)),corr/np.max(corr),label='Measured')
plt3.xlabel('Time Delay (ms)')
plt3.ylabel('Autocorrelation')
plt3.grid()
##plt3.xlim(1/sample_rate/1e-3,samp/sample_rate/1e-3)
plt3.savefig("Exp1_awgn_Autocorrelation" + ".png", bbox_inches='tight', pad_inches=0.5)
plt3.close()
print("Processing complete.\n")
