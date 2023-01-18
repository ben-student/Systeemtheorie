
import numpy as np
import matplotlib.pyplot as plt



f = 2 #hz
fs = 10 #hz samplerate

fs_cont = 100
Ts_cont = 1/fs_cont
tvec_cont = np.arange(-1,3,Ts_cont)
y_cont=np.sin(2*np.pi*f*tvec_cont)


N = np.array([10,11,12,13,14,15])

for i in range(len(N)):  
   
  
    Tend = N[i]/fs
    print(Tend)
    tvec = np.arange(0,Tend,1/fs)
    print(tvec)
    y = np.sin(2*np.pi*f*tvec)

    plt.figure(1)
    plt.subplot(len(N),2,(2*i)+1)
    plt.plot(tvec,y,'r*-')
    plt.plot(tvec_cont,y_cont,':k')
    plt.ylabel('y(T)')
    plt.xlabel('Time(s)')



    fvec = np.arange(0,fs,fs/N[i])
    Y = np.fft.fft(y)
    
    


    plt.figure(1)
    plt.subplot(len(N),2,(2*i)+2)
    plt.stem(fvec,np.abs(Y))
    plt.ylabel('|Y|')
    plt.xlabel('Freq (Hz)')


plt.show()
