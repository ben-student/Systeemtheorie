from db import db
import numpy as np
import matplotlib.pyplot as plt



f = 80 #hz
A = 1 #Amplitude
fs = 1000 #Hz
Ts = 1/fs
N = 32
T = N/fs

phi = np.pi/2


Tvec = np.arange(0,T,Ts)

y = A*np.sin(2*np.pi*f*Tvec+phi)

plt.figure(1)
plt.subplot(221)
plt.plot(Tvec,y, 'k:*')


Y = np.fft.fft(y)/N
Fvec = np.arange(0,fs,fs/N)


plt.subplot(222)
plt.plot(Fvec,db(Y),'b*')
plt.ylabel("Amplitude db")
plt.xlabel("Frequency (Hz)")


plt.subplot(223)
plt.plot(Fvec,np.abs(Y), 'b*')
plt.ylabel('amplitude LIN')
plt.ylabel('amplitude LIN')

plt.subplot(224)
plt.plot(np.abs(Y), 'b*')
plt.ylabel('amplitude LIN')
plt.xlabel("DFT lijnnummer")


plt.show()