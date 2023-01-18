from oef2 import N,wvec,wRes,H
import numpy as np
import matplotlib.pyplot as plt


Wres = wvec[1]-wvec[0]
fRes = wRes/(2*np.pi)
fs = fRes*N
Ts = 1/fs


tvec = np.arange(0,N*Ts,Ts)

Hhalf = H.copy()
Hhalf[int(np.round(N/2)):] = 0

h = 2*np.real(np.fft.ifft(Hhalf))


plt.figure(1)
plt.plot(tvec,h)
plt.xlabel('Time(s)')
plt.ylabel('h(t)')

plt.show()
plt.close()