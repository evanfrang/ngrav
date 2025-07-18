import numpy as np
from ngrav.integrators import RK4Integrator

class System:

    def __init__(self, bodies: list):
        self.bodies = bodies
        self.time = 0.0
        self.integrator = RK4Integrator(self)

    """def compute_accel(self):
        positions = np.array([b.position for b in self.bodies])
        masses = np.array([b.mass for b in self.bodies])

        accels = self.Forces.compute_vec_accel(positions, masses)
        for body, a in zip(self.bodies, accels):
            body.acceleration = a"""
        
    def masses(self):
        return np.array([b.mass for b in self.bodies])

    def initial_state(self):
        positions = np.array([b.position for b in self.bodies])
        velocities = np.array([b.velocity for b in self.bodies])
        return {'positions': positions, 'velocities': velocities}
    
    def run(self, sim_time, dt):
        steps = int(sim_time / dt)
        for _ in steps:
            self.step(dt)
