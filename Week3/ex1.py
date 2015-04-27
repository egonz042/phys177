"""
Exercise 1 Week 3
"""

from scipy import constants as sp
import numpy as np
import matplotlib.pyplot as plt

#Define variables and geometry

q1 = 1.							#Charge 1 in coulombs
q2 = -1.						#Charge 2 in coulombs
K = (1./((sp.epsilon_0)*(sp.pi)))	#Electric Constant
"""
dimensions of the density map, 101 to account for python indexing
"""
dim = 101						#100 cm dimensions
x01 = 50. - 5.						
x02 = 50. + 5.
y01 = 50.
y02 = y01

Phi = np.zeros(shape = (dim,dim)).astype('float')
for i in range(dim):
	y = float(i)					#y pos in cm, rows
	for j in range(dim):
		x = float(j)
#Potential at x,y accounting for units
		if(x==x01 and y==y01):
			V1 = 0
		else:
			V1 = K * q1 / (((((x-x01)/100.)**2)+(((y-y01)/100.)**2))**.5)	
		if(x==x02 and y==y02):
			V2 = 0
		else:
			V2 = K * q2 / (((((x-x02)/100.)**2)+(((y-y02)/100.)**2))**.5)
		Phi[i,j] = V1 + V2
#Plot the Potential density map
plt.subplot(3,1,1)
plt.imshow(Phi,origin='lower',extent=([0,dim,0,dim]))
plt.gray()

#Find the gradient of the function



GradPhiX = np.zeros(shape = (dim,dim)).astype('float')
GradPhiY = np.zeros(shape = (dim,dim)).astype('float')

#The gradient is the difference between the last point and the next, divided by the step
for k in range(1,dim-1):	
	GradPhiX[:,k] = (Phi[:,k+1] - Phi[:,k-1])/2.
	GradPhiY[k,:] = (Phi[k+1,:] - Phi[k-1,:])/2.

	
plt.subplot(3,1,2)
plt.quiver(GradPhiX,GradPhiY)

N = np.sqrt(GradPhiX**2+GradPhiY**2)
NGradPhiX = GradPhiX/N
NGradPhiY = GradPhiY/N
plt.subplot(3,1,3)
plt.quiver(NGradPhiX,NGradPhiY)
