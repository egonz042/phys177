import numpy as np
import matplotlib.pyplot as plt

VA = np.array([[4,-1,-1,-1],[-1,3,0,-1],[-1,0,3,-1],[-1,-1,-1,4]],dtype=float)
Vb = np.array([5,0,5,0],dtype=float)

#Gaussian Elimination

L = len(Vb)

for i in range(L):
	div = VA[i,i]
	VA[i,:] /= div
	Vb[i] /= div
	
	for j in range(i+1,L):
		mult = VA[j,i]
		VA[j,:] -= mult*VA[i,:]
		Vb[j] -= mult*Vb[i]

x = np.empty(L,float)
for k in range(L-1,-1,-1):
	x[k] = Vb[k]
	for l in range(k+1,L):
		x[k] -= VA[k,l]*x[l]

print x

y = np.linalg.solve(VA,Vb)

print y
