import numpy as np
import matplotlib.pyplot as plt
from db import db
# tau=0.5
# f= 1
# w = 2*np.pi*f
# H = 1/(1+1j*w*tau)


p1 = -0.1+10*1j #Wn = 10 = 0.1
p2 = -0.1-10*1j #Wn = 10 = 0.1

epsilon = 0.1
wn = 10
wRes= 0.1
wvec = np.arange(0,1000,wRes) #omega?
fvec = wvec/(2*np.pi) #=> omega = 2*pi*f | f = omega/(2*pi) 

N = len(wvec)

s = 1j*wvec
H = 1/((s-p1)*(s-p2))




#bodeplot
plt.figure(1)
plt.subplot(2,1,1)
plt.semilogx(wvec,db(H))
plt.xlabel('Angular Frequency (rad/s)')
plt.ylabel('Amplitude (db)')
plt.subplot(2,1,2)
plt.semilogx(wvec,np.angle(H))
plt.xlabel(' Angular Frequency (rad/s)')
plt.ylabel('Fase (rad)')


plt.figure(2)
plt.plot(np.real(p1),np.imag(p1),'bx')
plt.plot(np.real(p2),np.imag(p2),'bx')
plt.plot([-10,5],[0,0],'k')






plt.show()
plt.close()

