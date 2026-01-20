class Particle:
    def __init__(self, position, velocity):
        self.position = position
        self.velocity = velocity
    
    def update_state(self, dt, acceleration):
        self.velocity += dt * acceleration
        self.position += dt * self.velocity