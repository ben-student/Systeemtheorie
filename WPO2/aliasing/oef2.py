import numpy as np
import matplotlib.pyplot as plt




f = np.array([2,4,6,8,5,12]) #hz
N = 10
Tend = 1  #tijdsduur
Ts = Tend/N


Tvec = np.arange(0,Tend,Ts)


N_cont = 1000
Ts_cont = Tend/N_cont

Tvec_cont = np.arange(0,Tend,Ts_cont)



for i in range(len(f)):

    y = np.sin(2*np.pi*f[i]*Tvec)

    y_cont = np.sin(2*np.pi*f[i]*Tvec_cont)


    plt.subplot(3,3,i+1)
    plt.plot(Tvec, y, 'r--*')
    plt.plot(Tvec_cont, y_cont, 'k')
    plt.xlabel(str(f[i])+ 'Hz')
    plt.ylabel('Amplitude')







    


plt.show()


