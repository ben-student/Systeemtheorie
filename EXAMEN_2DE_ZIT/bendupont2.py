import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#LOG FUNCTIE
def db(x):
    x = 20*np.log10(np.abs(x))
    return x


Data = pd.read_csv("Data.csv")
Ureal = Data['Ureal']
Uimag = Data['Uimag']
U = Ureal + 1j*Uimag

fvec = Data['fvec']

print(Data)




plt.figure(1)
plt.semilogx(fvec,db(U))
plt.xlabel('Frequency (f)')
plt.ylabel('Amplitude (V)')
plt.tight_layout()



#Frequentie domein naar tijdsdomein
u = np.fft.ifft(U)


plt.figure(2)
plt.plot(fvec,u)
plt.xlabel('Tijd')
plt.ylabel('Amplitude (V)')
plt.tight_layout()

plt.show()