import pandas as pd
import numpy as np
import matplotlib.pyplot as plt



plt.close('all')

#IMPORT DATA FROM CSV
Data = pd.read_csv('Impuls_Dupont.csv')
h = Data['h']


#LOG FUNCTIE
def db(x):
    x = 20*np.log10(np.abs(x))
    return x

#1. PLOT IN TIMEDOMAIN
N = len(h)
fs = 100 #Hz
ts = 1/fs
tEnd = N/fs
tVec = np.arange(0,tEnd,ts)

plt.figure(1)
plt.plot(tVec,h)
plt.xlabel('Time(s)')
plt.ylabel('Amplitude')
plt.tight_layout()




#3. BODEPLOT
fNiquist = 50 #Hz (helft van sample frequentie)
fResNiquist = fNiquist/N #Resolutie nodig voor fVec op te maken
fVecNiquist = np.arange(0,fNiquist,fResNiquist)  #Frequentievector
wVec = np.pi*fVecNiquist  #Frequentievector omgezet naar hoeksnelheid


plt.figure(2)
plt.subplot(211)
plt.plot(wVec,db(h),'k')
plt.xlabel('Angular frequency (rad/s)')
plt.ylabel('Amplitude (db)')
plt.subplot(212)
plt.plot(wVec,np.angle(h),'g')
plt.xlabel('Angular frequency (rad/s)')
plt.ylabel('Fase (rad)')
plt.tight_layout()

#4. SINUS AANLEGGEN

f = 0.05 #Hz
A = 10 #amplitude
u = 10*np.sin(2*np.pi*f*tVec) #Sinus signaal aanmaken

U = np.fft.fft(u) #ingangssignaal naar Frequentiedomein

H = np.fft.fft(h) #ImpulsRespons naar Frequentiedomein


Y = U*H #Uitgangssignaal is gelijk aan het product van ingang u(t) en impulsrespons h(t) in het frequentiedomein

fRes = fs/N
fVec = np.arange(0,fs,fRes)



plt.figure(3)
plt.subplot(211)
plt.title("Input U(t) ")
plt.plot(fVec,db(U))
plt.xlabel("Frequency(Hz)")
plt.ylabel('Amplitude')
plt.subplot(212)
plt.title('Output Y(t)')
plt.plot(fVec,db(Y))
plt.xlabel("Frequency(Hz)")
plt.ylabel('Amplitude')
plt.tight_layout()





plt.show()
