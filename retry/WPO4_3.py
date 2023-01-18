from cProfile import label
import numpy as np
import matplotlib.pyplot as plt


fs = 1024
Ts = 1/fs
f1 = 20.5
f2 = 200.5

Tvec = np.arange(0,1,Ts)
N = len(Tvec)

u = np.sin(2*np.pi*f1*Tvec) #+ (10*np.exp(-4)) * np.sin(2*np.pi*f2*Tvec)




plt.figure(1)
plt.plot(Tvec,u,':',label='u(t)')



window = np.hamming(N)

u_h = np.multiply(u,window)

plt.plot(Tvec,window,label="window")
plt.plot(Tvec,u_h,'b',label="window*u(t)")
plt.legend()


plt.show()