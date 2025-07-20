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
        self.velocity_log = {body.id: [] for body in self.bodies}
        self.a_thresh = 100.
        self.dist_thresh = 100.
        self.collision_tolerance = 0.01
        
    def _log_current_positions(self, state):
        positions = state['positions']
        velocities = state['velocities']
        for i, pos in enumerate(positions):
            vel = velocities[i]
            self.trajectories[self.bodies[i].id].append(pos.copy())
            self.velocity_log[self.bodies[i].id].append(vel.copy())

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
            self._log_current_positions(state)
            if collision_detect(state['positions'], self.collision_tolerance):
                break
            if slingshot_detect(state, accel, self.a_thresh, self.dist_thresh):
                break
        if s < steps - 1:
            print(f"Simulation ended early at step {s}.")
        else:
            print(f"Simulation completed all {steps} steps.")
    
    def get_trajectories(self):
        return self.trajectories, self.velocity_log
