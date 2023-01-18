import numpy as np
import matplotlib.pyplot as plt

plt.close('all')


#A
L = ["A", 0, "B" ]

print(L[1])

#B
A = np.array([11, 2, 30])
B = np.zeros((3,3))
C = np.arange(0,100,1)

print(A)
print('B is een ' + str(B.shape[0]) + ' x '  + str(B.shape[1]) + ' Matrix')
print(C)



#C
#Dictionary
Dict = {}
Dict['L'] = L
Dict['A'] = A
Dict['getal'] = 3

print('uit dict: '  + str(Dict['getal']))



