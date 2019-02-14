import scipy as sy
import scipy.signal
import numpy as np
import matplotlib.pyplot as plt

upper = 2*np.pi
lower = 0
step = 0.001
var = []
var.append(np.arange(lower, upper+step, step))
var.append(sy.signal.sawtooth(var[0]+(np.pi/2), 0.5))
#var.append(sy.signal.square(var[0]+(np.pi/2), 0.5))

term = np.zeros(len(var[0]))
for n in range(1, 6, 2):
    An = (1/np.pi)*np.sum(var[1]*np.sin(n*var[0]))*step
    term = term + An*np.sin(n*var[0])
    # term = An*np.sin(n*var[0])
    # print(An)
    plt.plot(var[0], term, label="a"+str(n))
    # Bn = (1/np.pi)*np.sum(var[1]*np.cos(n*var[0]))*step
    # term = term + Bn*np.cos(n*var[0])
    #term = Bn*np.cos(n*var[0])
    # print(Bn)
    # plt.plot(var[0], term)
plt.plot(var[0], var[1], label="triangle wave")
plt.legend()
plt.show()
