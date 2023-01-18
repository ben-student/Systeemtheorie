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
tEnd = 2 # seconden
Ts = 0.01 # seconden -> Sample periode
f = 1 # frequentie
tvec = np.arange(0,tEnd,Ts) # tijdsvector 0 ≤ t < tEnd met een stapgrootte van Ts
y = np.sin(2*np.pi*f*tvec)
plt.figure()
plt.plot(tvec,y,'-*')
plt.xlabel('t')
plt.ylabel('y')


plt.show()