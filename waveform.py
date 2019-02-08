import scipy as sy               # this program numerically integrates var[1] to get the fourier series terms
import scipy.signal              # however, var[1] must have a range(upper-lower) of size 2pi in order for this to work
import numpy as np
import matplotlib.pyplot as plt


# The x and y axis's are a two dimensional list called var

# Generation of the y axis
upper = 2*np.pi
lower = 0
step = 0.001
var = []
var.append(np.arange(lower, upper+step, step))  

# Generation of triangle wave used in calculating the Fourier coefficents
var.append(sy.signal.sawtooth(var[0]+(np.pi/2), 0.5))

# The 0th term is empty
term = np.zeros(len(var[0]))

for n in range(1, 11):
    # Calculate coefficient for nth term of series
    An = (1/np.pi)*np.sum(var[1]*np.sin(n*var[0]))*step
    # Calculate new wave
    wave = An*np.sin(n*var[0])
    # Add the newly calculated wave to series
    term = term + wave
    # plot the newly calculated functions
    plt.plot(var[0], wave)
    plt.plot(var[0], term)

# Display the plot with all functions shown
plt.show()
