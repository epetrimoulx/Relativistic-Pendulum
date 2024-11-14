from scipy.integrate import odeint
import matplotlib.pyplot as plt
import numpy as np

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
    plt.ticklabel_format(style = "scientific", useMathText=True, axis="x", scilimits=(0,0))
    plt.show()
    
    return 0

def ODE(r, t):
    #constants
    speedOfLight = 299792458 #[m/s]
    gravitationalConstant = 6.67E-11 #[N m^2/kg^2]
    mass = 8.154E36 #[kg]
    massObject = 0.00005 #[kg]
    angularMomentum = 1E15#[kg m^2/s]
    
    q = r[0] #intial position
    w = r[1] #initial velocity
    
    relativisticTerm = (1 - (w**2)/(speedOfLight**2)) / (np.sqrt(np.abs(1 - (w**2)/(speedOfLight**2))) + w/(speedOfLight**2) * np.sqrt(np.abs( 1 - (w**2)/(speedOfLight**2))))**(-1)
    dqdt = w
    dwdt = ((angularMomentum**2)/ (massObject**2 * q**3) * relativisticTerm) - (gravitationalConstant*mass / q**2)* relativisticTerm
    
    return [dqdt, dwdt]
    
# initial conditions:
r0 = [10000000000000.0, 1000]

# time vector
time = np.linspace(0.0, 1000000, 150000)

r = odeint(ODE, r0, time)
q = r[:, 0]
w = r[:, 1]

print(r)

MakeGraph(time, q, 'time [s]', 'position [m]', 'Trajectory of a Relativistic Particle Near Sagittarius-A')
MakeGraph(time, w, 'time [s]', 'velocity [m/s]', 'Velocity of a Relativistic Particle Mear Sagittarius-A')
