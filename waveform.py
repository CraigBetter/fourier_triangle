import scipy as sy               # this program numerically integrates var[1] to get the fourier series terms
import scipy.signal              # however, var[1] must have a range(upper-lower) of size 2pi in order for this to work
import numpy as np
import matplotlib.pyplot as plt

upper = 2*np.pi
lower = 0
step = 0.001
var = []
var.append(np.arange(lower, upper+step, step))  # the x and y axis's are a two dimensional list called var
var.append(sy.signal.sawtooth(var[0]+(np.pi/2), 0.5))
#var.append(sy.signal.square(var[0]+(np.pi/2), 0.5))

term = np.zeros(len(var[0]))
for n in range(1, 11):
    An = (1/np.pi)*np.sum(var[1]*np.sin(n*var[0]))*step
    term = term + An*np.sin(n*var[0])
    plt.plot(var[0], term)
    #Bn = (1/np.pi)*np.sum(var[1]*np.cos(n*var[0]))*step
    #term = term + Bn*np.cos(n*var[0])
    #plt.plot(var[0], term)
plt.plot(var[0], term)

#plt.plot(var[0], var[1])
plt.show()
