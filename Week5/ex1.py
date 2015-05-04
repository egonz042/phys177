"""
Exercise 1 Week 5
"""

import numpy as np
import matplotlib.pyplot as plt

#Define P(x)

def poly(x):
	P = (924.*(x**6.)) - (2772.*(x**5.)) + (3150.*(x**4.)) - (1680.*(x**3.)) + (420.*(x**2.)) - (42.*x) + 1.
	return P

#Plot between 1 and 0, save as png

x = np.arange(0,1,0.01)
f = np.zeros(len(x))
f[:] = poly(x[:])
plt.plot(f)
plt.show()
plt.savefig('Polynomial.png',format='png')

#Guess .03, .17, .38, .62, .83, .96

g = np.array([0.03,0.17,.38,.62,.83,.96])

#Use Newton's Method to approximate to 1e-10

l = len(g)
root = np.zeros(l)

for i in range(l):
	j = 0
	r0 = g[i].copy()

	while (j==0):
		h = 0.005				#h step in derivative
		ff = poly(r0)				#P(x)
		fp = (poly(r0+h) - poly(r0-h))/(2*h)	#P'(x)
		r0 = r0 - (ff/fp)		#Newton's Method
		check = abs(ff/fp)			#Error approx.
		if check < 1e-10:
			root[i] = r0
			j = 1
		else:
			pass
print 'The roots of the polynomial are:\n {0:11}\n {1:11}\n {2:11} \n {3:11}\n {4:11}\n {5:11}\nWith an error less than 1e-10.'.format(root[0],root[1],root[2],root[3],root[4],root[5])
