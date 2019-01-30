

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Fixing random state for reproducibility
np.random.seed(19680801)


# Create new Figure with black background
fig = plt.figure(figsize=(8, 8), facecolor='black')

# Add a subplot with no frame
ax = plt.subplot(111, frameon=False)

data = np.zeros((11, 100))
X = np.linspace(-1, 1, data.shape[-1])
G = 3 #* np.exp(-4 * X ** 2)
bottom = 20
coef_persp = 1.3
coef_pitch = 0.4

# Generate line plots
lines = []
for i in range(len(data)):
    # perspective
    xscale = 1 + i**coef_persp / 50.
    lw = 1.5 + i**coef_persp / 20.0
    line, = ax.plot(xscale * X, i + G * data[i], color="w", lw=lw)
    lines.append(line)

# Set y limit (or first line is cropped because of thickness)
ax.set_ylim(-1, 30)

# No ticks
ax.set_xticks([])
ax.set_yticks([])

# 2 part titles to get different font weights
ax.text(0.5, 1.0, "TRIANGLE WAVE ", transform=ax.transAxes,
        ha="right", va="bottom", color="w",
        family="sans-serif", fontweight="light", fontsize=16)
ax.text(0.5, 1.0, "EXPERIENCE", transform=ax.transAxes,
        ha="left", va="bottom", color="w",
        family="sans-serif", fontweight="bold", fontsize=16)

def negatizer(arg):
    return (-1)**arg

def coef(arg):
    return (1+(2*arg))**-2


def update(frame, *args):

    x = frame / 10.0
    # Shift all data to the right
    data[:, 1:] = data[:, :-1]

    # Fill-in new values
    #for i,dat in enumerate(data):
      #dat[0] = np.sin(frame*.02*(i+1))

    coef_compound = (1-np.cos(frame/200.0)) * 0.5
    #coef_compound = ( np.sqrt(81*abs(np.cos(x)))*np.cos(x)/abs(np.cos(x)) +1 ) / 18
    # Update data
    for i in range(len(data)):
        if i == 0:
          data[i,0] = (8/(np.pi**2))*negatizer(i)*coef(i)*np.sin((1+i*2)*x)
        else:
          data[i,0] = coef_compound * data[i-1, 0] + (8/(np.pi**2))*negatizer(i)*coef(i)*np.sin((1+i*2)*x)

        lines[i].set_ydata( bottom - coef_pitch*i**coef_persp + G * (1+i**coef_persp/6.0) * data[i])

    # Return modified artists
    return lines

# Construct the animation, using the update function as the animation director.
anim = animation.FuncAnimation(fig, update, interval=10)
plt.show()


