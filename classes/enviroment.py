import numpy as np

class Enviroment:
    def __init__(self):
        self.gravity = 9.81
        
    def get_acceleration(self, particle=None):
        return np.array([0, -self.gravity])