import matplotlib.pyplot as plt
import numpy as np

def negatizer(arg):
    return (-1)**arg

def coef(arg):
    return (1+(2*arg))**-2

# upper = (np.pi/2)+0.1
# lower = (np.pi/2)-0.1
upper = 2*np.pi
lower = 0
step = 0.01
x = np.arange(lower, upper+step, step)

# y = (8/np.pi**2)*((np.sin(x))-((3**(-2))*np.sin(3*x))+((5**(-2))*np.sin(5*x))-((7**(-2))*np.sin(7*x))) # this works
# plt.plot(x,y)

y = (8/(np.pi**2))*(np.sin(x))
plt.plot(x,y)
for i in range(1, 10):
    y = y + (8/(np.pi**2))*negatizer(i)*coef(i)*np.sin((1+i*2)*x)
    plt.plot(x,y)
# y = (8/(np.pi**2))*y
# plt.plot(x,y)
plt.show()
