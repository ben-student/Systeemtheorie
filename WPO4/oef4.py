
import numpy as np
import matplotlib.pyplot as plt


p1 = -0.1+5*1j
p2 = -0.1-5*1j
p3 = -3

n1 = -2



nullen = np.roots([10,50,3])

polen = np.roots([1,6,630.2,3125])

plt.figure(1)
for n in range(len(nullen)):
    plt.plot(np.real(nullen[n]),np.imag(nullen[n]),'bo')

for p in range(len(nullen)):
    plt.plot(np.real(nullen[p]),np.imag(nullen[p]),'bx')


plt.plot([-6,2],[0,0], 'k-')
plt.plot([0,0],)


plt.show()