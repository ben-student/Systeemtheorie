import numpy as np
import matplotlib.pyplot as plt
from db import db
tau=0.5
# f= 1
# w = 2*np.pi*f
# H = 1/(1+1j*w*tau)




wRes= 0.1
wvec = np.arange(0,100,wRes) #omega?
fvec = wvec/(2*np.pi) #=> omega = 2*pi*f | f = omega/(2*pi) 

N = len(wvec)

s = 1j*wvec
H = 1/(1+1j*wvec*tau)


H3db = 1/(1+1j)

#bodeplot
plt.figure(1)
plt.subplot(2,1,1)
plt.semilogx(wvec,db(H))
plt.xlabel('Angular Frequency (rad/s)')
plt.ylabel('Amplitude (db)')
plt.plot(1/tau, db(H3db), 'ro')
plt.subplot(2,1,2)
plt.semilogx(wvec,np.angle(H))
plt.plot(1/tau, np.angle(H3db), 'ro')
plt.xlabel(' Angular Frequency (rad/s)')
plt.ylabel('Fase (rad)')


plt.show()

