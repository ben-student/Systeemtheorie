#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  5 09:37:25 2020
@author: user
"""
import numpy as np
import matplotlib.pyplot as plt
# close all figures
plt.close('all')
def db(x):
    x = 20*np.log10(np.abs(x))
    return x
p1 = -0.1+5*1j
p2 = -0.1-5*1j
fs = 100
fRes = 0.01
fvec = np.arange(0,fs,fRes)
wvec = np.pi*fvec
N = len(wvec)
s = 1j*wvec
H = 1/((s-p1)*(s-p2))
# Bode diagram
plt.figure(1)
plt.subplot(211)
plt.semilogx(wvec,db(H))
plt.xlabel('Angular Frequency (rad/s)')
plt.ylabel('Amplitude (dB)')
plt.subplot(212)
plt.semilogx(wvec,np.angle(H))
plt.xlabel('Angular Frequency (rad/s)')
plt.ylabel('Fase (rad)')
# Polen Nullen map
plt.figure(2)
plt.plot(np.real(p1),np.imag(p1),'bx')
plt.plot(np.real(p2),np.imag(p2),'bx')
plt.plot([-10,5],[0,0],'k-')
plt.plot([0,0],[-10,10],'k-')
plt.xlim(-10,5)
plt.ylim(-10,10)
# Opstellen tijdsvector in overeenstemming met de frequentievector
tvec = np.arange(0,N/fs,1/fs)
Hhalf = H.copy()
Hhalf[int(np.round(N/2)):] = 0 # stel het deel na fs/2 gelijk aan 0
h = 2*np.real(np.fft.ifft(Hhalf))
plt.figure(3)
plt.plot(tvec,h)
# Bereken de output via een convolutie
f = 1
tvec = np.arange(0,30/f,1/fs) # 30 periodes, tijdsvector van input signaal moet volgens dezelfde fs worden opgesteld als het impulsrespons
N = len(tvec)
u = np.sin(2*np.pi*f*tvec)
y = np.convolve(h,u)
y = y[0:N] # De convolutie genereert 2N-1 punten waarvan de eerste N zinvol zijn.
plt.figure(4)
plt.plot(tvec,u,'b')
plt.plot(tvec,y,'r')
NP = int(fs/f) # sampels per periode
yLast = y[N-NP:]
ySteady_state = np.tile(yLast,30) # Herhaal laatste periode 30 keer -> benadering van de steady state oplossing
plt.plot(tvec,y-ySteady_state,'k') # Plot de transient


plt.show()