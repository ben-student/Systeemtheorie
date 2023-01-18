#hanning venster



import numpy as np
import matplotlib.pyplot as plt


def db(x):
    x = 20*np.log10(np.abs(x))
    return x


fs =1024
N = 1024


f1 = 20.5 #hz
f2 = 200.5 #hz


tvec = np.arange(0,N/fs,1/fs)
fvec= np.arange(0,fs,fs/N)


u = np.sin(2*np.pi*f1*tvec)+10*np.exp(-4)*np.sin(2*np.sin*tvec*f2)
U = np.fft.fft(u)/N


plt.figure(6)
plt.subplot(211)
plt.plot(fvec, db(U))
plt.xlabel('Frequency (Hz)')
plt.ylabel('|U| (db)')
plt.xlim([0,fs/2])



window = np.hanning(N)
uHanning = np.multiply(u,window)

Uhanning = np.fft.fft(uHanning)/N

plt.subplot(212)
plt.plot(fvec,db(Uhanning))
plt.xlabel('Frequency (Hz)')
plt.ylabel('|U| (db)')
plt.xlim(0,fs/2)


plt.figure(7)
plt.plot(tvec,Uhanning)
plt.plot(tvec,u,':')
plt.plot(tvec,window,'r')
plt.xlabel('Time')
plt.ylabel('u(n)')
plt.legend('u(n)window','u(n)','window')
