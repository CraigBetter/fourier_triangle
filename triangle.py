import matplotlib.pyplot as plt
import numpy as np

def negatizer(arg):
    rep = (-arg)**2
    return rep

upper = 10
lower = -10
step = 0.01
x = np.arange(lower, upper+step, step)

# y = (8/np.pi**2)*((np.sin(x))-((3**(-2))*np.sin(3*x))+((5**(-2))*np.sin(5*x))-((7**(-2))*np.sin(7*x))) # this works

dummy = np.zeros((upper - lower)/step)
for i in range(1, 5):
    dummy = dummy + negatizer(i)*coef(i)*np.sin((1+i*2)*x)
y = (8/(np.pi**2))*dummy
plt.plot(x,y)
plt.show()
