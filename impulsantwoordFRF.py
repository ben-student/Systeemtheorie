import numpy as np
import matplotlib.pyplot as plt
import sys
# close all figures
plt.close('all')
def db(x):
    x = 20*np.log10(np.abs(x))
    return x
# 5.1: eerste orde systeem
tau = 0.5
wvec = np.arange(0,100,0.01)
N = len(wvec)
H = 1/(1+1j*wvec*tau)
H3db = 1/(1+1j)
plt.figure(1)
plt.subplot(211)
plt.semilogx(wvec,db(H))
plt.xlabel('Angular Frequency (rad/s)')
plt.ylabel('Amplitude (dB)')
plt.plot(1/tau,db(H3db),'ro')
plt.subplot(212)
plt.semilogx(wvec,np.angle(H))
plt.plot(1/tau,np.angle(H3db),'ro')
plt.xlabel('Angular Frequency (rad/s)')
plt.ylabel('Fase (rad)')
# 5.2: Tweede orde systeem
wn = 10
ksi = 0.1
wvec = np.arange(0,1000,0.1)
N = len(wvec)
H = (wn**2)/(-wvec**2+2*ksi*wn*1j*wvec+wn**2)
p1 = -ksi*wn+wn*np.sqrt(complex(ksi**2-1)) # to avoid nan for sqrt of negative 

p2 = -ksi*wn-wn*np.sqrt(complex(ksi**2-1))
plt.figure(2)
plt.subplot(211)
plt.semilogx(wvec,db(H))
plt.plot([np.imag(p1),np.imag(p1)],[-100,20],'r')
plt.xlabel('Angular Frequency (rad/s)')
plt.ylabel('Amplitude (dB)')
plt.subplot(212)
plt.semilogx(wvec,np.angle(H))
plt.plot(np.imag(p1),-np.pi/2,'ro')
plt.xlabel('Angular Frequency (rad/s)')
plt.ylabel('Fase (rad)')
plt.figure(3)
plt.plot(np.real(p1),np.imag(p1),'bx')
plt.plot(np.real(p2),np.imag(p2),'bx')
plt.plot([-10,5],[0,0],'k-')
plt.plot([0,0],[-15,15],'k-')
plt.xlim(-10,5)
plt.ylim(-15,15)
# sys.exit()
# impulse response
wRes = wvec[1]-wvec[0]
fRes = wRes/(2*np.pi)
fs = fRes*N
Ts = 1/fs
tvec = np.arange(0,N*Ts,Ts)
Hhalf = H.copy()
Hhalf[int(np.round(N/2)):] = 0
h = 2*np.real(np.fft.ifft(Hhalf))
plt.figure(4)
plt.plot(tvec,h)
plt.xlabel('Time (s)')
plt.ylabel('h(t)')
# 5.3.1: FRF op basis van polen en nullen
p1 = -0.1+2*5*1j
p2 = -0.1-2*5*1j
p3 = -3
p4 = -0.1-10*1j
p5 = -0.1+10*1j
n1 = -2
wRes = 0.1
wvec = np.arange(0,100,wRes)
N = len(wvec)
s = 1j*wvec
H = (s-n1)/((s-p1)*(s-p2)*(s-p3)*(s-p4)*(s-p5))
#H = (s-n1)
plt.figure(5)
plt.subplot(211)
plt.semilogx(wvec,db(H))
plt.xlabel('Angular Frequency (rad/s)')
plt.ylabel('Amplitude (dB)')
plt.subplot(212)
plt.semilogx(wvec,np.angle(H))
plt.xlabel('Angular Frequency (rad/s)')
plt.ylabel('Fase (rad)')
plt.figure(6)
plt.plot(np.real(p1),np.imag(p1),'bx')
plt.plot(np.real(p2),np.imag(p2),'bx')
plt.plot(np.real(p3),np.imag(p3),'bx')
plt.plot(np.real(p4),np.imag(p4),'bx')
plt.plot(np.real(p5),np.imag(p5),'bx')
plt.plot(np.real(n1),np.imag(n1),'bo')
plt.plot([-10,5],[0,0],'k-')
plt.plot([0,0],[-10,10],'k-')
plt.xlim(-10,5)
plt.ylim(-10,10)
fRes = wRes/(2*np.pi)
fs = fRes*N
Ts = 1/fs
tvec = np.arange(0,N*Ts,Ts)
Hhalf = H.copy()
Hhalf[int(np.round(N/2)):] = 0
h = 2*np.real(np.fft.ifft(Hhalf))
plt.figure(7)
plt.plot(tvec,h)
plt.xlabel('Time (s)')
plt.ylabel('h(t)')
plt.show()

