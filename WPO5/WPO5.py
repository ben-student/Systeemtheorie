# -*- coding: utf-8 -*-
"""
Created on Mon Nov 15 18:16:58 2021

@author: Peter De Winne
@email: peter.de.winne@vub.be
@studentnumber: 0556725
@education: bachelor industrial siences
"""
    
import numpy as np
import matplotlib.pyplot as plt
def oefening1():
    plt.close('all')
    #deel 1
    #gegeven polen
    p1 = -1 + 2*np.pi*5*1j
    p2 = -1 - 2*np.pi*5*1j
    K = (2*np.pi*5)**2
    Fs = 100
    Ts = 1/Fs
    N = 10**4
    Tend = N*Ts
    
    tvec = np.arange(0,Tend, Ts)
    fvec = np.arange(0, Fs, Fs/(N))
    wvec = 2*np.pi*fvec
    s = 1j*wvec
    
    H = K/((s-p1)*(s-p2))
    
    #deel 2
    Hhalf = H.copy()
    Hhalf[np.round(int(N/2)):] = 0
    
    h = 2*np.fft.ifft(Hhalf)
    
    plt.figure(1)
    plt.plot(tvec,h)
    plt.xlabel('time')
    plt.ylabel('h(t)')
    plt.show
    
    #deel 3
    Tvec = np.arange(0,20,Ts)
    n = len(Tvec)
    u = np.sin(2*np.pi*0.5*Tvec)
    
    #hoe doet ge dit?????????????????????????????????????????????
    y = np.convolve(u,h, mode = 'full')
    transient = y[n:n*2]
    y = y[0:n]
    
    
    plt.figure(2)
    plt.plot(Tvec, u, 'b-', label = 'Input')
    plt.plot(Tvec,y, 'r-', label  = 'Output')
    plt.plot(Tvec, transient, 'k-', label = 'Transient')
    plt.legend()
    plt.plot()

 
    
def oefening2():
    plt.close('all')
     #deel 1
    p1 = -4 + 100*1j
    p2 = -4 - 100*1j
    n = -100
    K = 100
    Fs = 1000
    Ts = 1/Fs
    N = 2560
    Tend = N*Ts
    
    tvec = np.arange(0,Tend,Ts)
    fvec = np.arange(0,Fs,Fs/N)
    wvec = 2*np.pi*fvec
    s = 1j*wvec
    
    H = K*(s-n)/((s-p1)*(s-p2))
    
    Hhalf = np.copy(H)
    Hhalf[np.round(int(N/2)):] = 0
    
    h = 2*np.fft.ifft(Hhalf)
    
    #deel 2
    u = np.cos(2*np.pi*tvec*3.125)
        #f berekenen met n = Ts*N/T
    y = np.convolve(u,h, mode = 'full') 
    Tvec = np.arange(0,(N*Ts*2),Ts)
    
    plt.figure(1)
    plt.plot(Tvec[:-1],y)
    plt.title('Convolutie met np.convolve')
    plt.show()
    
    y_tran = y[N-1:]
    y = y[0:N]
    y_steady = y + y_tran

    
    plt.figure(1)
    plt.plot(tvec, y, 'r-', label = 'Ouput')
    plt.plot(tvec, y_steady, 'k--', label = 'Steady state')
    plt.legend()
    plt.xlabel('Time (s)')
    plt.ylabel('y(t)')
    plt.plot()
    
    plt.figure(2)
    plt.plot(tvec, y_tran, 'k-', label = 'Transient')
    plt.xlabel('Time (s)')
    plt.ylabel('Transient')
    plt.plot()
    
    Y_conv = np.fft.fft(y)/N
    Y_steady = np.fft.fft(y_steady)/N
    
    plt.figure(3)
    plt.plot(fvec, dB(Y_conv), 'r+', label = 'Spectrum of the output')
    plt.plot(fvec, dB(Y_steady), 'g.', label = 'Spectrum of the steady')
    plt.xlim(-10,510)
    plt.legend()
    plt.show()
    
    
    #deel 4     
    U = np.fft.fft(u)
    
    Y = U*H
    
    plt.figure(4)
    plt.plot(fvec, dB(Y_conv), 'r+', label = 'Output from convolution')
    plt.plot(fvec, dB(Y), 'b.', label = 'Ouput from Y(S) = H(S)*U(S)')
    plt.xlabel('Frequency')
    plt.ylabel('|Y| (dB)')
    plt.legend()
    plt.show()
    
    
    Yhalf = np.copy(Y)
    Yhalf[np.round(int(N/2)):0] = 0
    y_spec = 2*np.fft.ifft(Yhalf)
    
    plt.figure(5)
    plt.plot(tvec, y, 'r-', label = 'Ouput')
    plt.plot(tvec, y_spec, 'b-', label = 'Output from ifft')
    plt.legend()
    plt.show()
    
def dB(H):
    return 20*np.log10(H)

def main():
    oefening1()
    oefening2()

if __name__ == '__main__':
    main()