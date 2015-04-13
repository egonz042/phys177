"""
Week 2 Example 1
"""

import numpy as np
import matplotlib.pyplot as plt


def trapFunc(x,y):
	dx = (x[1] - x[0])			#also h, trap spacing
	k = 1					#sum index
	TI = dx * 0.5 * (y[0] + y[-1])		#start I with end values
	kmax = x.size-1
	for k in range(kmax):
		TI += dx * y[k]
		k += 1
	return TI

def sampFunc(w,z):
	dw = (w[1] - w[0])
	j = 1.
	SI = dw * (1./3.) * (z[0] + z[-1])
	jmax = w.size-1
	for j in range(jmax):
		if (j % 2 == 0):
			SI += (4./3.) * dw * z[j]
			j+=1
		else:
			SI += (2./3.) * dw * z[j]
			j+=1
	return SI


def sampFuncVarRange(w,z,u):
	dw = (w[1] - w[0])
	j = 1.
	jmax = u
	SI = dw * (1./3.) * (z[0] + z[u])
	for j in range(jmax):
		if (j % 2 == 0):
			SI += (4./3.) * dw * z[j]
			j+=1
		else:
			SI += (2./3.) * dw * z[j]
			j+=1
	return SI




