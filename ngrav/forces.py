import numpy as np

class Gravity:
    def __init__(self, G=6.67430e-11, softening=1e-3):
        self.G = G
        self.softening = softening
    
    def compute(self, state, masses):
        positions = state['positions']
        delta = positions[np.newaxis, :, :] - positions[:, np.newaxis, :]
        dist_sqr = np.sum(delta**2, axis=2) + self.softening**2
        dist_cubed = dist_sqr * np.sqrt(dist_sqr)
        np.fill_diagonal(dist_cubed, np.inf)

        masses_j = masses[np.newaxis, :]
        force_mag = self.G * masses_j / dist_cubed
        forces = force_mag[:, :, np.newaxis] * delta
        accelerations = np.sum(forces, axis=1)
        
        return accelerations