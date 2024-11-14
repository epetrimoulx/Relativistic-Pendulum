from scipy.integrate import odeint
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation
from matplotlib.animation import PillowWriter



# Plot Graph:
def MakeGraph(x, y1, xlabel, ylabel, title):
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.plot(x, y1, color = 'black')
    plt.minorticks_on()
    plt.tick_params(which = 'minor', direction = 'in', bottom = True, top = True, left = True, right = True, length = 4)
    plt.tick_params(length = 7, bottom = True, top = True, left = True, right = True)
    plt.tick_params(axis = 'both', direction = 'in')
    plt.show()
    
    return 0

def ODE(theta, t, length):
    #constants
    speedOfLight = 299792458.0 #[m/s]
    gravity = 9.91 #[m/s^2]
    
    q = theta[0] #intial position
    w = theta[1] #initial velocity
    
    dqdt = w
    dwdt = (gravity * q / length * np.sqrt(1 - (w/speedOfLight)**2)**3) / (speedOfLight**2 - (length * w)**2 + w**2)
    
    return [dqdt, dwdt]

def animate(i, x, y, scat):
  scat.set_offsets([x[i],y[i]])
  line.set_xdata([0,x[i]])
  line.set_ydata([0,y[i]])

# initial conditions:
theta = [2, 25000]
length = 100 #[m]

# time vector
time = np.linspace(0, 1, 2000)

theta = odeint(ODE, theta, time, args=(length,))
q = theta[:, 0]
w = theta[:, 1]

x = length * np.sin(q)
y = length * np.cos(q)

MakeGraph(x, y, 'x position [m]', 'y position [m]', 'Pendulum Trajectory')
MakeGraph(time, q, 'time [s]', r'$\theta$', r'$\theta$ vs Time')

time = np.linspace(0, 0.000005, 2000)

fig, ax = plt.subplots()
ax.set(xlim = (-110, 110), ylim = (-110, 110))
scat = ax.scatter(x[0],y[0])
line = ax.plot([0,x[0]], [0,y[0]])[0]
ax.set_title('Relativistic Pendulum')
ax.set_xlabel('Displacement in horizontal [m]')
ax.set_ylabel('Displacement in vertical [m]')
ani = FuncAnimation(fig, animate, fargs = (x,y, scat), frames = 30, interval = 1)
ani.save('animation.gif', writer='imagemagick', fps=30)
plt.show()


