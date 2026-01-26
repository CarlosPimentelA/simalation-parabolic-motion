# main.py - Simulacion de tiro parabolico
import numpy as np
import matplotlib.pyplot as plt
from classes.particle import Particle
from classes.enviroment import Environment
from matplotlib.animation import FuncAnimation

# Estilo del grafico
plt.style.use('seaborn-v0_8-darkgrid')
COLOR_TRAYECTORIA = '#FF6B6B'
COLOR_PUNTOS = '#4ECDC4'

obj_mov = []
tiempos = []  # almacenar el tiempo en cada punto

print("=" * 50)
print("SIMULACIÓN DE MOVIMIENTO PARABÓLICO")
print("=" * 50)

initial_velocity = float(input("Velocidad inicial(m/s): "))
theta = float(input("Grados de inclinacion: "))
initial_distance = float(input("Posicion en x inicial(m): "))
initial_height = float(input("Posicion en y inicial(m): "))
mass = float(input("Masa de la pelota (kg): "))

print("\n--- Parámetros de resistencia del aire (ENTER para valores por defecto) ---")
air_density = input(f"Densidad del aire (kg/m³) [1.225]: ")
drag_coefficient = input(f"Coeficiente de arrastre [0.47 (esfera)]: ")
cross_sectional_area = input(f"Área transversal (m²) [0.05]: ") 

# Si no introduce parametros pone lo suyos por default
air_density = float(air_density) if air_density else 1.225
drag_coefficient = float(drag_coefficient) if drag_coefficient else 0.47
cross_sectional_area = float(cross_sectional_area) if cross_sectional_area else 0.05

environment = Environment(
    gravity=9.81,
    air_density=air_density,
    drag_coefficient=drag_coefficient,
    cross_sectional_area=cross_sectional_area
)

velocity_x = initial_velocity * np.cos(np.deg2rad(theta))
velocity_y = initial_velocity * np.sin(np.deg2rad(theta))

# ================= CONFIGURACIoN DE LA SIMULACIoN =================
dt = 0.01  # cuanto menor dt, mayor precision (0.01s = 10ms)
tiempo_total = 0  # iniciar contador de tiempo

# Definir vectores de estado inicial
position = np.array([initial_distance, initial_height])
velocity = np.array([velocity_x, velocity_y])

# Crear particula con estado inicial
particle = Particle(position, velocity, mass, environment)

# ================= BUCLE DE SIMULACION =================
while particle.position[1] >= 0:
    particle.update_state_rk4(tiempo_total, dt)
    
    # Guardar copia de la posicion actual para graficar
    obj_mov.append(particle.position.copy())
    # Guardar tiempo actual
    tiempos.append(tiempo_total)
    tiempo_total += dt

# ================= PROCESAMIENTO DE DATOS =================
# Extraer coordenadas
x_axis = [pos[0] for pos in obj_mov]
y_axis = [pos[1] for pos in obj_mov]

# Calcular métricas importantes
alcance_maximo = x_axis[-1] - initial_distance
altura_maxima = max(y_axis)
tiempo_vuelo = tiempo_total
velocidad_final = np.linalg.norm(particle.velocity)

# Encontrar el punto de altura máxima
altura_max = np.argmax(y_axis)
x_altura_max = x_axis[altura_max]
y_altura_max = y_axis[altura_max]

print("\n" + "=" * 50)
print("RESULTADOS DE LA SIMULACION")
print("=" * 50)
print(f"• Velocidad inicial: {initial_velocity} m/s")
print(f"• Angulo de lanzamiento: {theta}°")
print(f"• Tiempo de vuelo: {tiempo_vuelo:.2f} segundos")
print(f"• Alcance horizontal total: {alcance_maximo:.2f} metros")
print(f"• Altura maxima alcanzada: {altura_maxima:.2f} metros")
print(f"• Velocidad final de impacto: {velocidad_final:.2f} m/s")
print("=" * 50)

# ================= VISUALIZACION =================
# Crear la base del gráfico
fig, ax = plt.subplots()
ax.set_xlim(0, max(x_axis) * 1.05)
ax.set_ylim(0, max(y_axis) * 1.1)

# La coma después del nombre (linea,) es necesaria porque ax.plot devuelve una lista
linea, = ax.plot([], [], color=COLOR_TRAYECTORIA, lw=2)
punto, = ax.plot([], [], 'o', color='#EF476F', markersize=10)

def update(i):
    # 'i' irá desde 0 hasta el final de tus datos
    # Actualizamos la línea con todos los puntos hasta el actual 'i'
    linea.set_data(x_axis[:i], y_axis[:i])
    # Actualizamos el punto solo con la posición actual
    punto.set_data([x_axis[i]], [y_axis[i]])
    return linea, punto

ani = FuncAnimation(fig, update, frames=len(x_axis), interval=10, blit=True, repeat=False)

plt.axhline(y=altura_maxima, color='gray', linestyle='--', alpha=0.5, linewidth=1)
plt.axvline(x=x_altura_max, color='gray', linestyle='--', alpha=0.5, linewidth=1)

plt.xlabel('Distancia horizontal (m)', fontsize=12, fontweight='bold')
plt.ylabel('Altura (m)', fontsize=12, fontweight='bold')
plt.title('TRAYECTORIA PARABOLICA CON RESISTENCIA DEL AIRE', fontsize=14, fontweight='bold', pad=20)
plt.grid(True, alpha=0.4)

margen_x = max(10, alcance_maximo * 0.1)
margen_y = max(10, altura_maxima * 0.1)
plt.xlim(initial_distance - margen_x, x_axis[-1] + margen_x)
plt.ylim(-5, altura_maxima + margen_y)

plt.tight_layout() # ajustar para que todo quepa
plt.show() # mostrar grafico