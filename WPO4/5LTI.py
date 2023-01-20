import numpy as np
import matplotlib.pyplot as plt
from db import db
import cmath


tau = 0.5

Wres =0.1


wVec = np.arange(0,100,Wres)
N=len(wVec)

Jw = 1j *wVec


H = 1/(1+Jw*tau)


y_3db = 1/tau

x_3db = 1/(1+1j)


plt.close()
plt.figure(1)
plt.subplot(211)
plt.semilogx(wVec,db(H))
plt.plot(y_3db,db(x_3db),'ro')
plt.ylabel('Amplitude (dB)')
plt.xlabel('Angular frequency (rad/s)')
plt.subplot(212)
plt.semilogx(wVec,np.angle(H))
plt.plot(y_3db,np.angle(x_3db),'ro')
plt.ylabel('Fase (rad')
plt.xlabel('Angular frequency (rad/s)')



#2de orde systeem

Wn = 10
chi = 0.1
wRes = 0.1

H = ((Wn**2)/(np.real(Jw**2)+2*chi*Wn*Jw+(Wn**2)))

p1 = -chi*Wn + Wn*cmath.sqrt((chi**2)-1)
p2 = -chi*Wn - Wn*cmath.sqrt((chi**2)-1)




plt.close()

plt.figure(1)
plt.subplot(211)
plt.semilogx(wVec,db(H))
plt.plot([np.imag(p1),np.imag(p1)],[-100,12],'r')
plt.xlabel('angular frequency (rad/s)')
plt.ylabel('Amplitude(dB)')
plt.subplot(212)
plt.semilogx(wVec,np.angle(H))
plt.plot(np.imag(p1),-np.pi/2,'ro')
plt.xlabel("Angular Frequency (rad/s)")
plt.ylabel("Fas (rad)")


#polen en nullen map
plt.figure(2)
plt.plot(np.real(p1),np.imag(p1),'bx')
plt.plot(np.real(p2),np.imag(p2),'bx')

plt.plot([-10,5],[0,0],'k-')
plt.plot([0,0],[-15,15],'k-')
plt.xlim(-10,5)
plt.ylim(-15,15)

fRes = wRes/(2*np.pi)
fs = fRes*N
Ts = 1/fs
tEnd = Ts*N
print(Ts)
print(tEnd)
tVec = np.arange(0,tEnd,Ts)


Hhalf = H.copy()
Hhalf[int(np.round(N/2)):]=0 #stel het deel na fs/2 gelijk aan nul

h = 2*np.real(np.fft.ifft(Hhalf)) #inverse fourier tranfsormatie van de transferfucntie H
#plotten in het tijdsomein
plt.figure(3)
plt.plot(tVec,h)
plt.xlabel('Time (s)')
plt.ylabel('h(t)')





plt.show()


