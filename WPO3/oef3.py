import numpy as np
import matplotlib.pyplot as plt
from db import db



f = 65 #Hz
A = 1 #Amplitude
w = 2*np.pi*f #omega 2pif
phi = np.pi/2 #Phi pi/2
N = 16 #aantal punten
fs = 1000 #SamplingFrequentie
Ts = 1/fs #stappentijd
Tend = N/fs #Eindtijd -> 0.0016seconden

Tvec = np.arange(0,Tend,Ts) # Tijdsvector aanmaken

u = A*np.sin(w*Tvec+phi) #signaal U aanmaken
U = np.fft.fft(u)/N #omzetten naar frequentiedomein a.d.h.v ingebouwde Fast fourie transformatie


fvec = np.arange(0,fs,fs/N) #Frequentie vector aanmaken


#plotten
plt.figure(1)
plt.subplot(2,2,1)
plt.plot(Tvec,u,'ko:')
plt.xlabel('Time (s)')
plt.ylabel('u(t)')
plt.subplot(2,2,2)
plt.plot(fvec,db(U),'b*')
plt.ylabel('Amplitude (db)')
plt.xlabel('Frequency (Hz)')
plt.subplot(2,2,3)
plt.plot(np.abs(U),'b*')
plt.subplot(2,2,4)
plt.ylabel('Amplitude (lin)')
plt.xlabel('Frequency (Hz)')
plt.plot(fvec,np.abs(U),'b*')
plt.ylabel('Amplitude (lin)')
plt.xlabel('Frequency (Hz)')



plt.show()


