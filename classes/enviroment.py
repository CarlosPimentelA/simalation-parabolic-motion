# environment.py
import numpy as np

class Enviroment:
    def __init__(self, gravity):
        # Aceleracion gravitacional: -9.81 m/s² (negativa hacia abajo)
        self.gravity = gravity
        
    def compute_acceleration(self):
        # Retorna vector aceleracion
        return np.array([0, -self.gravity])