import numpy as np
import matplotlib.pyplot as plt
import oef1

plt.close('all')


#OEF 5
#a


L = oef1.L
for i in range(len(L)):
    print(L[i])


#b

x = np.arange(-4,4,0.01) 
f = 4 - np.square(x)

plt.figure(7)
plt.plot(x,f,'b')


approx = np.zeros((x.shape[0],3))




for k in range(1,4):
    for i in range(len(x)):
        approx[i, k-1] = 16/(k*np.pi)**2*(-1)**(k+1)*np.cos(k*np.pi*x[i]/2)

k1_fourier = 8/3 + approx[:,0]
k2_fourier = 8/3 + approx[:,0]+approx[:,1]
k3_fourier = 8/3 + approx[:,0]+approx[:,1]+ approx[:,2]


plt.plot(x,k2_fourier,'k')
plt.plot(x,k3_fourier,'y')
plt.legend(('original f', 'k=2', 'k=3'))


plt.show()
