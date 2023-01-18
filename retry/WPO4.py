from turtle import numinput
import matplotlib.pyplot as plt
import numpy as np


f = 2.0 #hz
fs = 10.0 #sample freq
N = np.array([10,11,12,13,14,15])
Ts = 1.0/fs #time step

fs_cont = 100
Ts_cont = 1/fs_cont
Tvec_cont = np.arange(-1,3,Ts_cont)


y_cont = np.sin(2.0*np.pi*f*Tvec_cont)



for i in range(len(N)):
    
    T = N[i]/fs
    Tvec = np.arange(0,T,Ts)
    y = np.sin(2*np.pi*f*Tvec)



    plt.figure(1)
    plt.subplot(len(N),2,(2*i)+1)
    plt.plot(Tvec_cont,y_cont,'k:')
    plt.plot(Tvec,y,'r*-')
    plt.ylabel('y(T)')
    plt.xlabel('Time(s)')


    Y = np.fft.fft(y)

    Fvec = np.arange(0,fs,fs/N[i])

    plt.figure(1)
    plt.subplot(len(N),2,(2*i)+2)
    plt.stem(Fvec,np.abs(Y))
    plt.ylabel('|Y|')
    plt.xlabel('Freq (Hz)')






plt.show()