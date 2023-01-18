import numpy as np
import matplotlib.pyplot as plt


#a : exponentiele functies
a = 0.8
x = np.arange(0,1,0.2)
y = np.exp(-a*x)


#b : vrije val
def vrijeVal(z0, t):
    g =9.81
    z = z0 - g*np.square(t)/2

    return z

#c : figuren plotten


# (a)
plt.figure(1)
plt.plot(x,y)
plt.xlabel('x')
plt.ylabel('y')
plt.title("Exponential function")


# (b)
t = np.arange(0,3,0.01)
z1 = vrijeVal(100,t)
z2 = vrijeVal(75,t)

plt.figure(2)
plt.subplot(211)
plt.plot(t,z1,'b')
plt.xlabel('Time (s)')
plt.ylabel('z (m)')
plt.title('Vrije val')
plt.subplot(212)
plt.plot(t,z2, 'r')
plt.xlabel('Time (s)')
plt.ylabel('z (m)')
plt.title('Vrije val')


plt.show()
