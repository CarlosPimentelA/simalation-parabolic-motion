# main.py - Simulacion de tiro parabolico
import numpy as np
import matplotlib.pyplot as plt
from classes import particle
from classes import enviroment as env

# Lista para almacenar las posiciones del objeto en movimiento
obj_mov = []

# Crear instancia del entorno fisico
enviroment = env.Enviroment()

# ================= ENTRADA DE PARaMETROS INICIALES =================
# Velocidad: metros/segundo
# Distancia: metros
# Angulo: grados
initial_velocity = float(input("Velocidad inicial(m/s): "))
theta = float(input("Grados de inclinacion: "))
initial_distance = float(input("Posicion en x inicial(m): "))
initial_height = float(input("Posicion en y inicial(m): "))

# ================= DESCOMPOSICION VECTORIAL DE VELOCIDAD =================
velocity_x = initial_velocity * np.cos(np.deg2rad(theta))
velocity_y = initial_velocity * np.sin(np.deg2rad(theta))

# ================= CONFIGURACIoN DE LA SIMULACIoN =================
dt = 0.01  # Cuanto menor dt, mayor precision (0.01s = 10ms)

# Obtener aceleracion del entorno
acceleration = enviroment.get_acceleration()

# Definir vectores de estado inicial
position = np.array([initial_distance, initial_height])  # [x, y] en metros
velocity = np.array([velocity_x, velocity_y])  # [vₓ, vᵧ] en m/s

# Crear particula con estado inicial
particle = particle.Particle(position, velocity)

# ================= BUCLE DE SIMULACION =================
# Simular mientras la particula este por encima del suelo (y ≥ 0)
while particle.position[1] >= 0:
    # Actualizar estado de la particula
    particle.update_state(dt, acceleration)

    # Guardar copia de la posicion actual para graficar
    obj_mov.append(particle.position.copy())

# ================= PROCESAMIENTO DE DATOS =================
x_axis = []  # Lista de posiciones horizontales (m)
y_axis = []  # Lista de posiciones verticales (m)

for obj in obj_mov:
    x_axis.append(obj[0])  # Coordenada x en metros
    y_axis.append(obj[1])  # Coordenada y en metros

# ================= VISUALIZACION =================
plt.plot(x_axis, y_axis)
plt.title('Trayectoria Parabolica')  # Titulo del grafico
plt.xlabel('Distancia horizontal (m)')  # Eje x en metros
plt.ylabel('Altura (m)')  # Eje y en metros
plt.xlim(0, 500)  # Limite del eje x: 0 a 500 metros
plt.ylim(0, 500)  # Limite del eje y: 0 a 500 metros
plt.show()  # Mostrar grafico