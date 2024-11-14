from scipy.integrate import odeint
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation


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
    print(dqdt)
    gamma = (length*w/speedOfLight)**2
    dwdt = gravity * q * (1 - gamma) / (length * np.sqrt(np.abs(1 - gamma)) + gamma/length * np.sqrt(np.abs(1 - gamma))**(-1))
    
    return [dqdt, dwdt]



def animate(i, x, y, scat):
  scat.set_offsets([x[i],y[i]])
  line.set_xdata([0,x[i]])
  line.set_ydata([0,y[i]])
  # line.set_label(f"{(np.sqrt(x[i]**2 + y[i]**2))}")
  # plt.legend()

# initial conditions:
theta0 = [0.25* np.pi,100000]
length = 100 #[m]

# time vector
time = np.linspace(0, 20, 2000)

theta = odeint(ODE, theta0, time, args=(length,))
q = theta[:, 0]
w = theta[:, 1]

x = length * np.sin(q)
y = length * np.cos(q)

MakeGraph(x, y, 'time[s]', 'test', 'test')
MakeGraph(time, q, 'time [s]', 'position [m]', 'Position Pendulum')

time = np.linspace(0, 200, 2000)
MakeGraph(time, w, 'time [s]', 'velocity [m/s]', 'Velocity Pendulum')
MakeGraph(x, w, 'time [s]', 'velocity [m/s]', 'Velocity Pendulum')

fig, ax = plt.subplots()
ax.set(xlim = (-110, 110), ylim = (-110, 110))
scat = ax.scatter(x[0],y[0])
line = ax.plot([0,x[0]], [0,y[0]])[0]
ani = FuncAnimation(fig, animate, fargs = (x,y, scat), frames = 10000000, interval = 1)
plt.show()

#Normal Pendulum:
g = 9.81

theta2 = 0.25 * np.cos(np.sqrt(g/length) * time)
x = length * np.sin(theta2)
y = -length * np.cos(theta2)

MakeGraph(time, theta2, 'time [s]', 'position [m]', 'Position Pendulum')

fig, ax = plt.subplots()
ax.set(xlim = (-110, 110), ylim = (-110, 110))
scat = ax.scatter(x[0],y[0])
line = ax.plot([0,x[0]], [0,y[0]])[0]
ani = FuncAnimation(fig, animate, fargs = (x,y, scat), frames = 1000, interval = 10)

plt.show()