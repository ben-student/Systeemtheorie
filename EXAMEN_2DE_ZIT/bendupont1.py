import numpy as np
import matplotlib.pyplot as plt


#DB FUNCTIE

def db(x):
    x = 20*np.log10(np.abs(x))
    return x



#VARIABELEN
N = 10**4
fs = 100 #Hz
Ts = 1/fs
p1 = -5 + 1j
p2 = -5 - 1j
z1 = -10
K= 15
print(fs/(N))
Tend = N*Ts
#VECTOREN
tvec = np.arange(0,N/fs,Ts)
fvec = np.arange(0,fs,fs/(N))
wvec = 2*np.pi*fvec
s= 1j*wvec

# Laplace polen en nullen map
H = K*(s-z1)/((s-p1)*(s-p2))


# Bode diagram
plt.figure(1)
plt.subplot(211)
plt.title("Bode diagrams")
plt.semilogx(wvec,db(H))
plt.xlabel('Angular Frequency (rad/s)')
plt.ylabel('Amplitude (dB)')
plt.subplot(212)
plt.semilogx(wvec,np.angle(H))
plt.xlabel('Angular Frequency (rad/s)')
plt.ylabel('Fase (rad)')
plt.tight_layout()

#Nodige python computatie voor H functie te plotten
Hhalf = H.copy()
Hhalf[int(np.round(N/2)):] = 0 # stel het deel na fs/2 gelijk aan 0
h = 2*np.real(np.fft.ifft(Hhalf))




 

plt.figure(2)
plt.subplot(211)
plt.title("Input signaal H(t)")
plt.plot(tvec,h)
plt.xlabel('time (s)')
plt.ylabel('h(t)')
plt.subplot(212)
plt.plot(fvec,H)
plt.xlabel('frequency (Hz)')
plt.ylabel('h(t)')
plt.tight_layout()







#deel 2

f = 0.5 #Hz sinus freq
tvec = np.arange(0,25/f,1/fs)
N = len(tvec)
u = np.sin(2*np.pi*f*tvec)
y=np.convolve(h,u)
y = y[0:N]
h = h[0:N]
fvec = np.arange(0,fs,fs/(N))


plt.figure(3)
plt.subplot(311)
plt.title("Convolution y(t) = h(t) * u(t)")
plt.plot(tvec,u,'k',label='u(t)')
plt.plot(tvec,y,'y',label='y(t)')
plt.xlabel('time (s)')
plt.ylabel('amplitude (v)')
# plt.legend(loc="upper left")

H = np.fft.fft(h)
Y = np.fft.fft(y)
U = np.fft.fft(u)
plt.subplot(312)
plt.semilogx(fvec,db(H),'g',label='H(f)')
plt.semilogx(fvec,db(U),'b',label='U(f)')
plt.semilogx(fvec,db(Y),'r',label='Y(f)')
plt.xlabel('frequency (Hz) log')
plt.ylabel('amplitude (v) db')


plt.subplot(313)
plt.plot(fvec,H,'g',label='H(f)')
plt.plot(fvec,U,'b',label='U(f)')
plt.plot(fvec,Y,'r',label='Y(f)')
plt.xlabel('frequency (Hz) ')
plt.ylabel('amplitude (v)')










plt.tight_layout()
plt.show()

