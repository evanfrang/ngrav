from ngrav.system import System
from ngrav.forces import Gravity
from ngrav.integrators import RK4Integrator
import numpy as np
import matplotlib.pyplot as plt
from ngrav.body import Body

bodies = [
    Body(mass=1.0, position=[0.0, 0.0], velocity=[0.0, 0.0]),
    Body(mass=0.001, position=[1.0, 0.0], velocity=[0.0, 1.0]),
]

# Instantiate system and components
system = System(bodies)
forces = Gravity(G=1.0)
integrator = RK4Integrator(forces.compute)

# Initial state
state = system.initial_state()
masses = system.masses()
dt = 0.01
T = 100.0
steps = int(T / dt)

# Storage for visualization
trajectory = [state['positions'].copy()]

# Time loop
for step in range(steps):
    state = integrator.step(state, masses, dt)
    trajectory.append(state['positions'].copy())

trajectory = np.array(trajectory)  # shape (steps+1, N, 2)

# Plot the results
for i in range(len(bodies)):
    plt.plot(trajectory[:, i, 0], trajectory[:, i, 1])
plt.gca().set_aspect('equal')
plt.savefig("results/trajectory.png")