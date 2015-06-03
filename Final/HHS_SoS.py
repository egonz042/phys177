"""
Run 2 of Henon Heiles Potential model
"""

import numpy as np
import matplotlib.pylab as plt

# Define Functions

def U(r):
	x = r[0]
	y = r[1]
	U = 0.5*((x**2.)+(y**2.)+(2*(x**2.)*y)-(2./3.*(y**3.)))
	return U

def K(p):
	px = p[0]
	py = p[1]
	K = 0.5*((px**2.)+(py**2.))
	return K

def E(UE,KE):
	E = UE + KE
	return E

# Equations of Motion

def dr(p):
	dx = p[0]
	dy = p[1]
	return np.array([dx,dy],float)

def ddr(r):
	x = r[0]
	y = r[1]
	ddx = (-2.*x*y)-x
	ddy = (y**2.)-y-(x**2.)
	return np.array([ddx,ddy],float)

# Runge-Kutta Algorithm

def rk(s,h,a):
	s0 = s.copy()
	if(a == 0):
		k1 = h*dr(s0)
		k2 = h*dr(s0+(0.5*k1))
		k3 = h*dr(s0+(0.5*k2))
		k4 = h*dr(s0+(0.5*k3))
	else:
		k1 = h*ddr(s0)
		k2 = h*ddr(s0+(0.5*k1))
		k3 = h*ddr(s0+(0.5*k2))
		k4 = h*ddr(s0+(0.5*k3))
	k = (k1+(2.*k2)+(2.*k3)+k4)/6.
	return k

### Initial Conditions

E0 = 1./8.
Range = 100.
x0 = 0.
y0 = 0.
t = 0
tarAcc = 1e-4

### Surface of Selection Phase Spaces

# x(t) = 0

Xpx = []
Xy = []
Xpy = []

# y(t) = 0

Yx = []
Ypx = []
Ypy = []

# px(t) = 0

PXx = []
PXy = []
PXpy = []


# py(t) = 0

PYx = []
PYpx = []
PYy = []

### Iterate with different initial conditions

i = np.arange(20).astype('float')
i += 1.
j = 0

###I copied this over to reiterate because for some reason the nested while loop breaks the for loop. For now I brute force it but I will find a solution to clean it up

for j in range(20):

	px0 = np.sqrt(2.*E0)*(1.-(1./i[j]))
	py0 = np.sqrt((2.*E0)-(px0**2.))

	### Build Arrays & Lists

	r = np.array([x0,y0],float)
	p = np.array([px0,py0],float)

	tpoints = []

	while(t<Range):

		#Variable step size
		rho_y = 0.
		rho_x = 0.
		h = 0.01
		r0 = r.copy()
		p0 = p.copy()
		while(rho_y < 1. or rho_x < 1.):
			h /= 2.
			#One step of 2h
			r1 = r0.copy()
			r1 += rk(p0,(2.*h),0)
			#Two steps of h
			r2 = r0.copy()
			p2 = p0.copy()
			r2 += rk(p0,h,0)
			p2 += rk(r2,h,1)
			r2 += rk(p2,h,0)
			rho_x = ((30.*tarAcc)/(abs(r1[0]-r2[0])))
			rho_y = ((30.*tarAcc)/(abs(r1[1]-r2[1])))
		if rho_x > rho_y:
			hprime = h * (rho_y)**0.25
		else:
			hprime = h * (rho_x)**0.25
		r += rk(p0,hprime,0)
		p += rk(r,hprime,1)
		t += hprime
		tpoints.append(t)

		if(abs(r[0])<=1e-3):

			Xpx.append(p[0])
			Xy.append(r[1])
			Xpy.append(p[1])

		elif(abs(r[1])<=1e-3):

			Yx.append(r[0])
			Ypx.append(p[0])
			Ypy.append(p[1])

		elif(abs(p[0])<=1e-3):

			PXx.append(r[0])
			PXy.append(r[1])
			PXpy.append(p[1])
	
		elif(abs(p[1])<=1e-3):

			PYx.append(r[0])
			PYpx.append(p[0])
			PYy.append(r[1])
		print j,t



plt.subplot(1,1,1)
plt.plot(Xy,Xpy,'.')
