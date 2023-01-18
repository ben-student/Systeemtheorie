#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 12 15:46:20 2020
@author: Jan Decuyper
"""
import numpy as np # importeer de Numpy bib
import matplotlib.pyplot as plt # importeer de matplot bib
plt.close('all') # sluit alle openstaande figuren
# Voorbeeld



tEnd = 2 # seconden tEnd = N*Ts, dit is de breedte van het venster, N stapjes van de sample periode Ts

Ts = 0.1 # seconden -> Sample periode

f = 1 # frequentie van het signaal

tvec = np.arange(0,tEnd,Ts) # tijdsvector 0 ≤ t < tEnd met een stapgrootte van Ts

x = np.sin(2*np.pi*f*tvec) # bemonsterd signaal

plt.figure()
plt.plot(tvec,x,'-*')
plt.xlabel('t')
plt.ylabel('x(t)')


N = len(tvec) # het aantal punten waarop het discrete signaal berekend werd komt overeen met de lengthe van de tijdsvector

X = np.fft.fft(x)/N # berekenen van de DFT aan de hand van het FFT algoritme. 
# STEEDS schalen met N zodat de amplitude van het spectrum onafhankelijk wordt van het aantal gemeten punten.
fs = 1/Ts # 10 Hz
# De frequentievector komt overeen met de eerste N frequentielijnen uit de DFT. 
# Dit zijn de locaties waarop de FFT implementatie de DFT uitrekent (zie filpmje). 
# De dirac-kam die gebruikt wordt om het frequentiedomein te bemonsteren heeft een spasering van 1/tEnd -> 1/vensterbreedte, 1/tEnd = 1/(N*Ts) = fs/N
fvec = np.arange(0,fs,fs/N) # we hebben dus een vector van N punten, startend in 0 en lopend tot fs in stapjes van fs/N. 
# Merk op dat net zoals de tijdsvector, ook de frequentievector strikt kleiner blijft dan fs (laatste punt 1 stapje vroeger)
plt.figure()
plt.stem(fvec,np.abs(X),'r-') # hier mag je ook plot gebruiken in plaats van stem.
# Denk eraan dat een frequentiespectrum een reeks van complexe getallen is.
# We kiezen er hier voor om de grootte weer te geven aan de hand van de absolute waarde.
plt.xlabel('Frequentie (Hz)')
plt.ylabel('|X|')

plt.show()