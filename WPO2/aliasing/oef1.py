import numpy as np
import matplotlib.pyplot as plt


f = 1 #hz
N = 10 #aantal punten
T = 1/f #periode
Tend = f  #1 seconde tijdsduur
Ts = T/N #SampleRate

f2 = 9 #hz
Tvec = np.arange(0,Tend,Ts)


y1 = np.sin(2*np.pi*f*Tvec)
y2 = np.sin(2*np.pi*f2*Tvec)




plt.figure(1)
plt.title("Sample rate " + str(Ts))
plt.plot(Tvec, y1, '*')
plt.plot(Tvec, y2, '*r')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')



N2 = 1000
Ts2 = T/N2


Tvec2 = np.arange(0,Tend,Ts2)

y1_2 = np.sin(2*np.pi*f*Tvec2)
y2_2 = np.sin(2*np.pi*f2*Tvec2)

plt.figure(2)

plt.plot(Tvec2, y1_2, 'b')
plt.plot(Tvec, y1, '*')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')


plt.figure(3)
plt.title("Sample rate" + str(Ts2))
plt.plot(Tvec,y2,'*r')
plt.plot(Tvec2, y2_2, 'r')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')






plt.show()

