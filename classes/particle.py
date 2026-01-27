import numpy as np

class Particle:
    def __init__(self, position, velocity, mass, environment):
        self.position = position
        self.velocity = velocity
        self.env = environment
        self.mass = mass
    
    def update_state(self, dt, acceleration):
        # Metodo de Euler para integracion numerica
        self.velocity += dt * acceleration
        self.position += dt * self.velocity
        
    def state_derivatives(self, t, state):
        position = state[:2]
        velocity = state[2:]

        acceleration = self.env.compute_acceleration(velocity) # Velocidad necesaria
        return np.concatenate((velocity, acceleration))
    
    def update_state_rk4(self, t, dt):
        state = np.concatenate((self.position, self.velocity))
        k1 = self.state_derivatives(t, state)
        k2 = self.state_derivatives(t + dt/2, state + dt/2 * k1)
        k3 = self.state_derivatives(t + dt/2, state + dt/2 * k2)
        k4 = self.state_derivatives(t + dt, state + dt * k3)
        
        state_next = state + (dt/6)*(k1 + 2*k2 + 2*k3 + k4)
        
        self.position = state_next[:2]
        self.velocity = state_next[2:]