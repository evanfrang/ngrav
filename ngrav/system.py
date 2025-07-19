import numpy as np
from ngrav.integrators import RK4Integrator
from ngrav.collision_detection import collision_detect

class System:

    def __init__(self, bodies: list):
        self.bodies = bodies
        self.time = 0.0
        self.integrator = RK4Integrator(self)
        
    def masses(self):
        return np.array([b.mass for b in self.bodies])

    def initial_state(self):
        positions = np.array([b.position for b in self.bodies])
        velocities = np.array([b.velocity for b in self.bodies])
        return {'positions': positions, 'velocities': velocities}
    
    def run(self, sim_time, dt):
        steps = int(sim_time / dt)
        for _ in steps:
            #check collision
            collision_detect(self.bodies, dt)
            self.step(dt)
