"""
Week 2 Exercise 3
"""

from scipy import integrate as spi
import numpy as np
import matplotlib.pyplot as plt
import ex1 as Int

#initialize arrays to integrate
x = np.arange(21.)

x = x * 0.1

y = (x**4.) - (2. * x) + 1
#integrate with handmade functions & scipy
T = Int.trapFunc(x,y)

S = Int.sampFunc(x,y)

Tz = spi.trapz(y,x)

Ss = spi.simps(y,x)
#initialize error analysis arrays
w = np.arange(11)

w = w * 0.2

z = (w**4.) - (2. * w) + 1
#integrate to find error
Te = Int.trapFunc(w,z)
Se = Int.sampFunc(w,z)

Tze = spi.trapz(z,w)
Sse = spi.simps(z,w)

Error1 = (T - Te) * (1./3)
Error2 = (S - Se) * (1./15)
Error3 = (Tz - Tze) * (1./3)
Error4 = (Ss - Sse) * (1./15)


print 'The Trapezoidal Integral for the function is {0:.6}\n with an error of {1:.5}\n'.format(T,Error1)
print 'The Simpson Integral for the function is {0:.6}\n with an error of {1:.1}\n'.format(S,Error2)
print 'The Scipy Trapezoidal Integral for the function is {0:.6}\n with an error of {1:0.5}\n'.format(Tz,Error3)
print 'The Scipy Simpson Integral for the function is {0:.6}\n with an error of {1:0.1}\n'.format(Ss,Error4)

Ireal = 4.4

DiffT = T-Ireal
DiffS = S-Ireal

print 'The real value for the integral is {0:.3}'.format(Ireal)

print 'The Trapezoidal Integral has a second order error of {0:0.5}\nThe Simpson Integral has a fourth order error of {1:0.5}'.format(DiffT,DiffS)


