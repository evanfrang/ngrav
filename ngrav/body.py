import numpy as np

class Body:
    def __init__(self, mass, position, velocity, name=None, color='white', radius=1.0):
        self.mass = mass                         
        self.position = np.array(position, dtype=float)
        self.velocity = np.array(velocity, dtype=float)
        self.acceleration = np.zeros(2)  

        self.name = name
        self.color = color                         
        self.radius = radius                      
        self.trail = []