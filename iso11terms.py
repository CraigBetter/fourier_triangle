import scipy as sy
import scipy.signal
import numpy as np
from mpl_toolkits.mplot3d.axes3d import Axes3D
import matplotlib.pyplot as plt
from random import randint

fig, ax = plt.subplots(subplot_kw={'projection': '3d'})

upper = 2*np.pi
lower = 0
step = 0.001
var = []
var.append(np.arange(lower, upper+step, step))
var.append(sy.signal.sawtooth(var[0]+(np.pi/2), 0.5))

# col = []
# for i in range(22):
#    col.append('#%06X' % randint(1, 0xFFFFFF))
col = ['#F16C33', '#CAA46D', '#2CED02', '#A0BF8B', '#EB2EFD', '#D196AD', '#459DA1', '#30F866', '#2C8287', '#1A6991', '#41733D', '#E26CD4', '#9612BB', '#26787B', '#01AAC6', '#2034C2', '#2A4A27', '#6FF0B9', '#BC4813', '#A962D9', '#29867E', '#A6E5FA']

term = np.zeros(len(var[0]))
n = 0
datasets = [{"x":var[0], "y":NOTHING+n, "z":term, "colour":col[n]} for _ in range(1)]
for dataset in datasets:
    ax.plot(dataset["x"], dataset["y"], dataset["z"], color=dataset["colour"])
plt.plot(var[0], term, label="a0")
NOTHING = np.zeros(len(var[0]))
# for n in range(1, 11):
n = 1
b = 1
a = 1
while n <= 10:
    An = (1/np.pi)*np.sum(var[1]*np.sin(a*var[0]))*step
    # term = term + An*np.sin(n*var[0])
    term = An*np.sin(n*var[0])
    datasets = [{"x":var[0], "y":NOTHING+n, "z":term, "colour":col[n]} for _ in range(1)]
    for dataset in datasets:
        ax.plot(dataset["x"], dataset["y"], dataset["z"], color=dataset["colour"], label="a"+str(a))
    n = n+1
    a = a+1
    Bn = (1/np.pi)*np.sum(var[1]*np.cos(b*var[0]))*step
    # term = term + Bn*np.cos(n*var[0])
    term = Bn*np.cos(n*var[0])
    datasets = [{"x":var[0], "y":NOTHING+n, "z":term, "colour":col[n]} for _ in range(1)]
    for dataset in datasets:
        ax.plot(dataset["x"], dataset["y"], dataset["z"], color=dataset["colour"], label="b"+str(b))
    n = n+1
    b = b+1

plt.legend()
plt.show()
