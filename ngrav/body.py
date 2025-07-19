import numpy as np

class Body:
    def __init__(self, id, mass, position, velocity):
        self.id = id
        self.mass = mass                         
        self.position = np.array(position, dtype=float)
        self.velocity = np.array(velocity, dtype=float)
        self.acceleration = np.zeros(2)  