# particle.py
class Particle:
    def __init__(self, position, velocity):
        self.position = position
        self.velocity = velocity
    
    def update_state(self, dt, acceleration):
        # Metodo de Euler para integracion numerica
        self.velocity += dt * acceleration
        self.position += dt * self.velocity