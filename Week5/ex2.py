import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

def dft(y):
	N = len(y)
	c = np.zeros(N//2+1,complex)
	for k in range(N//2+1):
		for n in range(N):
			c[k] += y[n]*np.exp(-2j*np.pi*k*n/N)
	return c

t = np.arange(0,1,0.001)
N = float(len(t))

square_array = signal.square(2.*np.pi*t)
sawtooth_array = signal.sawtooth(2.*np.pi*t)
mod_saw_array = np.sin(np.pi*sawtooth_array/N) * np.sin(20*np.pi*sawtooth_array/N)

sq_coeff = dft(square_array)
sw_coeff = dft(sawtooth_array)
mod_sw_coeff = dft(mod_saw_array)
L = np.arange(len(sq_coeff))

plt.subplot(3,1,1)
plt.plot(L,abs(sq_coeff))
plt.subplot(3,1,2)
plt.plot(L,abs(sw_coeff))
plt.subplot(3,1,3)
plt.plot(L,abs(mod_sw_coeff))
plt.xlim(0,1000)
plt.show
