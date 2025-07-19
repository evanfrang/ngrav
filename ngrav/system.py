import numpy as np
from ngrav.integrators import RK4Integrator
from ngrav.collision_detection import collision_detect
from ngrav.slingshot_detection import slingshot_detect

class System:

    def __init__(self, bodies: list):
        self.bodies = bodies
        self.time = 0.0
        self.integrator = RK4Integrator(self)
        self.trajectories = {body.id: [] for body in self.bodies}
        
    def _log_current_positions(self, state):
        positions = state['positions']
        for i, pos in enumerate(positions):
            self.trajectories[self.bodies[i].id].append(pos.copy())

    def masses(self):
        return np.array([b.mass for b in self.bodies])

    def initial_state(self):
        positions = np.array([b.position for b in self.bodies])
        velocities = np.array([b.velocity for b in self.bodies])
        return {'positions': positions, 'velocities': velocities}
    
    def run(self, sim_time, dt):
        steps = int(sim_time / dt)
        state = self.initial_state()
        self._log_current_positions(state)
        for s in range(steps):
            state, accel = self.integrator.step(state, self.masses(), dt)
            if collision_detect(state['positions'], tolerance=0.1):
                break
            if slingshot_detect(accel, a_thresh=1000.):
                break
            self._log_current_positions(state)
        if s < steps - 1:
            print(f"Simulation ended early at step {s}.")
        else:
            print(f"Simulation completed all {steps} steps.")
    
    def get_trajectories(self):
        return self.trajectories
