"""
Week 2 Exericise 4
"""

import numpy as np
import ex1 as Int
import matplotlib.pyplot as plt

i = 1
k = 0
j = 0
Acc = 0.000001

x = np.arange(2)
y = ((np.sin(np.sqrt(100 * x)))**2)
I = Int.trapFunc(x,y)

a = float(x[-1])
while (j==0):
	Iold = I
	I *= 0.5
	for k in range(i):
		I += (((1./2.)**i) * ((2.**k)*a))
	E = (1./3.) * (I - Iold)

	print 'Iteration {0}:\n The integral was broken into {1} slices.\n The calculated value of the integral is {2:0.7}\n with a second order error of {3:0.3}.'.format(i,int(i*2),I,E)

	if (E < Acc):
		j = 1
	else:
		i += 1

print 'The integral was broken into {0} slices after {1} iterations\n to reach the desired accuracy of {2:0.5}\n with a value of {3:0.7}'.format(int(i*2),i,E,I)
