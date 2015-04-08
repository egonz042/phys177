"""
Interference Patterns
"""

import numpy as np
import matplotlib.pylab as plt
import math

# 1Define variables
# 2Define positions
# 3Compute image
# 4Graph

#1: Variables
ax=plt.subplot(111)
lambda_wave = 5. #wavelength in cm
k = 2. * np.pi / lambda_wave #wave number
xi = 1.          #amplitude in cm
separation = 20. #separation of sources in cm
size = 1. * 100. #size of pic in cm
npixel = 500.    #resolution
dx = size/float(npixel)

#2: Positions
x1c = size / 2. - separation / 2.
y1c = size / 2.
x2c = size / 2. + separation / 2.
y2c = size / 2. 

xi_both = np.zeros(shape=(npixel,npixel)).astype('float')

#3: Compute image
for j in range(int(npixel)):
	y=float(j)*dx
	for i in range(int(npixel)):
		x=float(i)*dx
		r1 = np.sqrt( (x-x1c)**2 + (y-y1c)**2)
		r2 = np.sqrt((x-x2c)**2+(y-y2c)**2)
		xi1 = xi*np.sin(k*r1)
		xi2 = xi*np.sin(k*r2)
		xi_both[j,i]=xi1+xi2

#4:Plot
plt.imshow(xi_both,origin='lower',extend=([0,size,0,size]))
plt.gray()
ax.set_xlabel('x [cm]')
ax.set_ylabel('y [cm]')

plt.savefig('newplot.png',format='png')
