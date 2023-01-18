import numpy as np
import matplotlib.pyplot as plt


#a


A = 2 #amplitude
f = 4 #hz
N = 100 #aantal punten


T = 1/f #periode
Ts = 2* T/N #sample periode of tijdstap (s) / stapgroote
Tend = 2 * T
tvec = np.arange(0,Tend,Ts) #tijdsvector
tvec = tvec.T #transpose zodat het kolomvector wordt
y = A*np.sin(2*np.pi*f*tvec) #(a*sin(2*pi*f*t)

plt.figure(1)
plt.plot(tvec,y)
plt.xlabel('Time ()s')
plt.ylabel('y (m)')


#b

N = 10 #aantal punten


Ts = 2* T/N #sample periode of tijdstap (s) / stapgroote
tvec = np.arange(0,Tend,Ts) #tijdsvector
tvec = tvec.T #transpose zodat het kolomvector wordt
y = A*np.sin(2*np.pi*f*tvec) #(a*sin(2*pi*f*t)

plt.figure(2)
plt.plot(tvec,y)
plt.xlabel('Time ()s')
plt.ylabel('y (m)')






# 'c'
f = 1
A=1
T=1
tvec = np.arange(0,1,0.01)

y = A*np.sin(2*np.pi*f*tvec)
yy = np.concatenate((y,y))

plt.figure(3)
plt.plot(yy)


#d

#comp 1
f1 =5
A1 = 20
#comp 2
f2 =15
A2 = 4

Ts = 0.001 #tijdsstap
T1 = 1/f1 #periode -> Berekend op laagste frequentie
Tend = 4*T1 #Aantal periodes


tvec = np.arange(0,Tend, Ts) #tijdsvector 0 tot Tend met stapgroote 0.001
y1 = A1*np.sin(2*np.pi*f1*tvec)  #Eerste sinuscomponent
y2 = A2*np.sin(2*np.pi*f2*tvec)  #Tweede sinuscomponent

y = y1+y2 #samenvoeging van beide sinuscomponenten
plt.figure(4)
plt.plot(tvec, y, 'y')
plt.xlabel('Time (s)')
plt.ylabel('y')


plt.show()


