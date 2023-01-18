
import numpy as np
import matplotlib.pyplot as plt




#Undersampling
T = 1.0 #s
f1 = 1.0 #Hz
N1 = 10.0 #punten
Ts= T/N1 #Timestep

Tvec1 = np.arange(0,T, Ts)


#Proper sampling

f2= 9.0 #Hz
N2 = 1000.0 #punten
Ts = T/N2 #timestep

Tvec2 = np.arange(0,T,Ts)

#Aliasing 
y2_alias= np.sin(2*np.pi*f2*Tvec1)

y1_alias = np.sin(2*np.pi*f1*Tvec1)

plt.figure(1)
plt.subplot(311)
plt.title("Aliasing occuring on f2")
plt.plot(Tvec1, y1_alias, 'g*')
plt.plot(Tvec1, y2_alias, 'b*')



y1_good = np.sin(2*np.pi*f1*Tvec2)

y2_good = np.sin(2*np.pi*f2*Tvec2)

#No aliasing
plt.subplot(312)
plt.title("F1 with 1000 points")
plt.plot(Tvec2,y1_good,"g")
plt.plot(Tvec1,y1_alias,"g*")


plt.subplot(313)
plt.title("f2 with 1000 points")
plt.plot(Tvec2,y2_good, "b")
plt.plot(Tvec1, y2_alias, "b*")






#PART2
plt.figure(2)

freqs = np.array([2,4,5,6,8,12])



for i in range(len(freqs)) : 
    y = np.sin(2*np.pi*freqs[i]*Tvec1)
    y_cont = np.sin(2*np.pi*freqs[i]*Tvec2)

    plt.subplot(3,2,1+i)
    plt.plot(Tvec1, y,'r-*')
    plt.plot(Tvec2,y_cont,"k")












plt.show()