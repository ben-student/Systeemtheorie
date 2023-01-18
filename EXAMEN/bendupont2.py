import numpy as np
import matplotlib.pyplot as plt


#LOG FUNCTIE
def db(x):
    x = 20*np.log10(np.abs(x))
    return x


#Tijdsvector opstellen
N = 50
fs = 10 #hz
tEnd = N/fs
ts = 1/fs
tVec = np.arange(0,tEnd,ts)


#Frequentievector opstellen

fRes = fs/N # 1/50 = 0.02 dus fRes is goed.

fVec = np.arange(0,fs,fRes)


print(fRes)


#Signaal opwerkken
f1 = 0.25 #Hz
f2 = 0.20 #Hz
u = np.sin(2*np.pi*f1*tVec) + np.sin(2*np.pi*f2*tVec)

#Testsignaal in tijdsdomein
plt.figure(1)
plt.plot(tVec,u, '*-')
plt.xlabel("Time(s)")
plt.ylabel("Amplitude")



#Frequentiedomein

U = np.fft.fft(u)

plt.figure(2)
plt.title("Frequency domain")
plt.plot(fVec,db(U))
plt.xlabel("Frequency(Hz)")
plt.ylabel("Amplitude")






plt.show()