import numpy as np 
import matplotlib.pyplot as plt



p1 = -1 + 2*np.pi*5j
p2 = -1 - 2*np.pi*5j
K = (2*np.pi*5)**2
f0 = 0
fs = 100 #sample rate
N = 10**4

Ts = 1/fs #period
Tend = N*Ts #number of samples times period

tVect = np.arange(0,Tend,Ts)
fVect = np.arange(0,fs,(fs/N))
s = 1j*2*np.pi*fVect

H = K/((s-p1)*(s-p2))

Hhalf = H.copy()
Hhalf[np.round(int(N/2)):] = 0

h = 2*np.fft.ifft(Hhalf)

plt.figure(1)
plt.plot(tVect,h)
plt.xlabel("time")
plt.ylabel("h(t)")
plt.show()


