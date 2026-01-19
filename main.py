import numpy as np
from classes import particle
from classes import enviroment as env


enviroment = env.Enviroment()
initial_velocity = float(input("Velocidad inicial: "))
theta = float(input("Grado de inclinacion: "))
initial_distance = float(input("Posicion en x inicial: "))
initial_height = float(input("Posicion en y inicial: "))
velocity_x = initial_velocity * np.cos(np.deg2rad(theta))
velocity_y = initial_velocity * np.sin(np.deg2rad(theta))

dt = 0.01
acceleration = enviroment.gravity
position = np.array([initial_distance, initial_height])
velocity = np.array([velocity_x, velocity_y])
particle = particle.Particle(position, velocity)

particle.update_state(dt, acceleration)