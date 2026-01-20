import numpy as np
import matplotlib.pyplot as plt
from classes import particle
from classes import enviroment as env

obj_mov = []
enviroment = env.Enviroment()
initial_velocity = float(input("Velocidad inicial: "))
theta = float(input("Grado de inclinacion: "))
initial_distance = float(input("Posicion en x inicial: "))
initial_height = float(input("Posicion en y inicial: "))
velocity_x = initial_velocity * np.cos(np.deg2rad(theta))
velocity_y = initial_velocity * np.sin(np.deg2rad(theta))

dt = 0.01
acceleration = enviroment.get_acceleration()
position = np.array([initial_distance, initial_height])
velocity = np.array([velocity_x, velocity_y])
particle = particle.Particle(position, velocity)


while particle.position[1] >= 0:
    particle.update_state(dt, acceleration)
    obj_mov.append(particle.position.copy())
    
x_axis = []
y_axis = []
for obj in obj_mov:
    x_axis.append(obj[0])
    y_axis.append(obj[1])
    
plt.plot(x_axis, y_axis)
plt.xlim(0,500)
plt.ylim(0,500)
plt.show()