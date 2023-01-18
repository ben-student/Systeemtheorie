import numpy as np
import matplotlib.pyplot as plt



f = 50 #Hz
fs = 1000 #Hz
Tend = 2
Ts = 1/fs


tvec = np.arange(0,2,Ts)
# y = np.sin(2*np.pi*f*tvec)
y = np.cos(2*np.pi*f*tvec)

#function DFT
Y = np.fft.fft(y)

#Own DFT
N = len(tvec)
print("N :", N)
Y_own = np.zeros(Y.shape[0],dtype=complex)
for k in range(N):
    for t in range(N):
        Y_own[k] += y[t]*np.exp(-2*1j*np.pi*k*t/N)


plt.figure(1)
plt.plot(np.abs(Y), 'ko-')
plt.plot(np.abs(Y_own), 'r*:')
plt.xlabel('k')
plt.ylabel('|Y|')
plt.legend(('FFT', 'Own DFT'))



#DFT in frequentiespectrum
fvec = np.arange(0,fs,fs/N)


plt.figure(2)
plt.plot(fvec,np.abs(Y), 'ko-')
plt.plot(fvec,np.abs(Y_own), 'r*:')
plt.xlabel('Frequentie')
plt.ylabel('|Y|')
plt.legend(('FFT', 'Own DFT'))
plt.show()