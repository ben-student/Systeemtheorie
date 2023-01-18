import numpy as np
import matplotlib.pyplot as plt



N = 32
A = 1
Tend = 1/f_NL
Ts = Tend/N
fs = 1/Ts




def db(x):
    x = 20*np.log10(np.abs(x))
    return x



phi = np.pi/2



tvec =np.arange(0,Tend,1/fs)


u = np.sin(2*np.pi*f*tvec+phi)
U = np.fft.fft(u)/N

plt.figure(2)
plt.subplot(221)
plt.plot(tvec,u,'k*:')


fvec = np.arange(0,fs,fs/N)

plt.figure(2)
plt.subplot(222)
plt.plot(fvec,db(U), '*')
plt.xlabel('Frequency')
plt.ylabel('Amplitude (db')


plt.subplot(223)
plt.plot(np.abs(U),'*')
plt.xlabel('DFT lijnnummer')
plt.ylabel('Amplitude (lin)')


plt.subplot(224)
plt.plot(fvec,np.abs(U),'*')
plt.xlabel('Frequency')
plt.ylabel('Amplitude (lin)')


