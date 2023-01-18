
import numpy as np
import matplotlib.pyplot as plt


f = 3 #Hz
fs = 10#hz
T = 2
Ts = 1/fs

Tvec = np.arange(0,T,Ts)
N = len(Tvec)


y = np.sin(2*np.pi*f*Tvec)


Y = np.fft.fft(y)

Y_own = np.zeros(Y.shape[0],dtype=complex)


for k in range(len(Tvec)):
    for t in range(len(Tvec)):
        Y_own[k] += y[t] * np.exp(-1j*2*np.pi*k*t/N)



Fvec = np.arange(0,fs, fs/N)


plt.subplot(211)
plt.title("Frequentie(Hz)")
plt.plot(Fvec, np.abs(Y_own),'ro-',label='Own_DFT')
plt.plot(Fvec,np.abs(Y), 'k*:', label="FFT")
plt.legend()


plt.subplot(212)
plt.title("K - as")
plt.plot(np.abs(Y_own),'ro-',label='Own_DFT')
plt.plot(np.abs(Y), 'k*:', label="FFT")
plt.legend()











plt.show()