# environment.py
import numpy as np

class Enviroment:
    def __init__(self):
        # Aceleracion gravitacional: -9.81 m/s² (negativa hacia abajo)
        self.gravity = 9.81
        
    def get_acceleration(self, particle=None):
        # Retorna vector aceleracion
        return np.array([0, -self.gravity])