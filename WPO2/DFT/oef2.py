import numpy as np
import matplotlib.pyplot as plt






f = np.array([2,4,6,8]) #hz
fs = 10
Tend = 1  #tijdsduur
Ts = 1/fs



Tvec = np.arange(0,Tend,Ts)
N = len(Tvec)

fvec = np.arange(0,fs,fs/N)

fs_cont = 1000
Ts_cont = 1/fs_cont

Tvec_cont = np.arange(0,Tend,Ts_cont)



for i in range(len(f)):
    #aliasing signaal
    y = np.sin(2*np.pi*f[i]*Tvec)
    Y = np.fft.fft(y)



    #continu signaal
    y_cont = np.sin(2*np.pi*f[i]*Tvec_cont)
    Y_cont = np.fft.fft(y_cont)



    #Plotten sinus
    plt.subplot(4,2,(2*i)+1)
    plt.plot(Tvec, y, 'r--*')
    plt.plot(Tvec_cont, y_cont, 'k')
    plt.xlabel(str(f[i])+ 'Hz')
    plt.ylabel('Amplitude')

    #Plotten DFT's 
    plt.subplot(4,2,(i*2)+2)
    plt.stem(fvec,np.abs(Y),'r')
    plt.xlabel(str(f[i])+ 'Hz')
    plt.ylabel('Amplitude')

plt.subplot(4,2,7)
plt.xlabel('Time(s)')
plt.subplot(4,2,8)
plt.xlabel('Frequency(Hz)')

plt.show()
    






    


plt.show()


