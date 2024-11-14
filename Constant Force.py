from scipy.integrate import odeint
import matplotlib.pyplot as plt
import numpy as np

# Plot Graph:
def MakeGraph(x, y1, xlabel, ylabel):
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.plot(x, y1, color = 'black')
    plt.minorticks_on()
    plt.tick_params(which = 'minor', direction = 'in', bottom = True, top = True, left = True, right = True, length = 4)
    plt.tick_params(length = 7, bottom = True, top = True, left = True, right = True)
    plt.tick_params(axis = 'both', direction = 'in')
    plt.show()
    
    return 0

def ODE(r, t):
    #constants
    speedOfLight = 299792458.0 #[m/s]
    k = -5000000.0 #[N/m]
    
    q = r[0] #intial position
    w = r[1] #initial velocity
    dqdt = w
    dwdt = -k * np.sqrt(1 - (w/speedOfLight)**2)**3 
    
    return [dqdt, dwdt]
    
# initial conditions:
r0 = [1, 2500000.0]

# time vector
time = np.linspace(0, 200, 100000)

r = odeint(ODE, r0, time)
q = r[:, 0]
w = r[:, 1]

# Normal Equations of Motion
k = -5000000.0 #[N/m]
a = k
v = k*time + r0[1]
position = 0.5 * k * time**2 + r0[1]*time + r0[0]


MakeGraph(time, q, 'Time [s]', 'Position [m]')
MakeGraph(time, w, 'Time [s]', 'Velocity [m/s]')

speedOfLight = 299792458.0 #[m/s]

gamma = (1 - (w/speedOfLight)**2)
a = (-k*gamma)/(np.sqrt(gamma) + (w/speedOfLight**2) * np.sqrt(gamma)**(-1))

MakeGraph(w, a, 'Velocity [m/s]', 'Acceleration [m/s^2]')
