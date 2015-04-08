"""
Lab 1 Example 3b
Ball drop with range of velocity
"""

import numpy as np
import matplotlib.pyplot as plt
import math

#1: Define variables

h = 800				#height of building in meters
g = 9.81			#acceleration due to gravity in m/s**2
bins = 10		        #bins
v = np.arange(10)	#velocity array set-up
t = np.zeros(10)
#2: Aquire velocity range

vmin = input("Enter the minimum velocity in meters per second: ")
vmin = float(vmin)
vmax = input("Enter the maximum velocity in meters per second: ")
vmax = float(vmax)
dv = (vmax-vmin) / bins

#3: Time to reach ground as a function of velocity

vmin = vmin + (dv/2)

v = vmin + (v * dv)

t += (-v + np.sqrt((v**2)+(2*g*h))) / g

np.savetxt('dropTime.txt',t,fmt='%5.2f') 

line = plt.plot(v,t,'o-',color='red')

plt.xlabel('Velocity [m/s]')
plt.ylabel('Time [s]')
plt.show()
