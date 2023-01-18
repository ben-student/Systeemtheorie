#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 12 15:46:20 2020
@author: Jan Decuyper
"""
import numpy as np # importeer de Numpy bib
import matplotlib.pyplot as plt # importeer de matplot bib
plt.close('all') # sluit alle openstaande figuren
def db(X): # omzetten naar decibel
    dbX = 20*np.log10(X)
    return dbX
# Voorbeeld
Ts = 0.01 # seconden -> Sample periode
f = 1 # frequentie van het signaal
tEnd = 10.5 # seconden tEnd = N*Ts, dit is een venster van 10.5 perioden
tvec = np.arange(0,tEnd,Ts) # tijdsvector 0 ≤ t < tEnd met een stapgrootte van Ts
x = np.sin(2*np.pi*f*tvec) # bemonsterd signaal
plt.figure(1)
plt.plot(tvec,x,'-*')
plt.xlabel('t (s)')
plt.ylabel('x(t)')
N = len(tvec) # het aantal punten waarop het discrete signaal berekend werd komt overeen met de lengthe van de tijdsvector
X = np.fft.fft(x)/N # berekenen van de DFT aan de hand van het FFT algoritme. 
# STEEDS schalen met N zodat de amplitude van het spectrum onafhankelijk wordt van et aantal gemeten punten.
fs = 1/Ts # 100 Hz
# De frequentievector komt overeen met de eerste N frequentielijnen uit de DFT. 
# Dit zijn de locaties waarop de FFT implementatie de DFT uitrekent (zie filpmje). 
# De dirac-kam die gebruikt wordt om het frequentiedomein te bemonsteren heeft een spasering van 1/tEnd -> 1/vensterbreedte, 1/tEnd = 1/(N*Ts) = fs/N
fvec = np.arange(0,fs,fs/N) # we hebben dus een vector van N punten, startend in 0 en lopend tot fs in stapjes van fs/N. 
# Merk op dat net zoals de tijdsvector, ook de frequentievector strikt kleiner blijft dan fs (laatste punt 1 stapje vroeger)
plt.figure(2)
plt.plot(fvec,db(X),'b-') # we plotten de grootte van het spectrum op een decibel schaal.
plt.xlabel('Frequentie (Hz)') # het spectrum vertoont leakage aangezien we geen geheel aantal perioden hebben opgemeten
plt.ylabel('|X| (dB)')
# Invoeren van een Hanning venster
window = np.hanning(N) # een hanning venster van N samples
xHanning = x*window # een weging met het hanning venster
XHanning = np.fft.fft(xHanning)/N # het spectrum van het gewogen signaal
plt.figure(2)
plt.plot(fvec,db(XHanning),'r') # het leakage effect wordt onderdrukt, we zien dat de vervorming van het spectrum sneller wegzakt

plt.show()