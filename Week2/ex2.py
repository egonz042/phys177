"""
Week 2 Exercise 2
"""

import numpy as np
import matplotlib.pyplot as plt
import ex1 as Int

t,x = np.loadtxt('velocities.txt', unpack=True)

T = Int.trapFunc(t,x)
S = Int.sampFunc(t,x)

print 'The Trapezoidal Integral for distance traveled is {0:.7}'.format(T)

print 'The Sampson Integral for distance traveled is {0:.7}'.format(S)

#distance curve

i = 1
j = t.size
d = np.zeros(j)

for i in range(1,j):
	dS = Int.sampFuncVarRange(t,x,i)
	d[i] += dS	

plt.subplot(2,1,1)
plt.plot(t,x,'o-',color='red')
plt.xlabel('Time [s]')
plt.ylabel('Velocity [m/s]')
plt.subplot(2,1,2)
plt.plot(t,d,'o-',color='blue')
plt.xlabel('Time [s]')
plt.ylabel('Distance [m]')
