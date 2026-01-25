# main.py - Simulacion de tiro parabolico
import numpy as np
import matplotlib.pyplot as plt
from classes import particle
from classes import enviroment as env
from matplotlib.animation import FuncAnimation

# Estilo del grafico
plt.style.use('seaborn-v0_8-darkgrid')
COLOR_TRAYECTORIA = '#FF6B6B'
COLOR_PUNTOS = '#4ECDC4'

# Lista para almacenar las posiciones del objeto en movimiento
obj_mov = []
tiempos = []  # almacenar el tiempo en cada punto

# Crear instancia del entorno fisico
enviroment = env.Enviroment()

# ================= ENTRADA DE PARaMETROS INICIALES =================
# Velocidad: metros/segundo
# Distancia: metros
# Angulo: grados
print("=" * 50)
print("SIMULACIÓN DE MOVIMIENTO PARABÓLICO")
print("=" * 50)

initial_velocity = float(input("Velocidad inicial(m/s): "))
theta = float(input("Grados de inclinacion: "))
initial_distance = float(input("Posicion en x inicial(m): "))
initial_height = float(input("Posicion en y inicial(m): "))

# ================= DESCOMPOSICION VECTORIAL DE VELOCIDAD =================
velocity_x = initial_velocity * np.cos(np.deg2rad(theta))
velocity_y = initial_velocity * np.sin(np.deg2rad(theta))

# ================= CONFIGURACIoN DE LA SIMULACIoN =================
dt = 0.01  # cuanto menor dt, mayor precision (0.01s = 10ms)
tiempo_total = 0  # iniciar contador de tiempo

# Definir vectores de estado inicial
position = np.array([initial_distance, initial_height])
velocity = np.array([velocity_x, velocity_y])

# Crear particula con estado inicial
particle = particle.Particle(position, velocity, enviroment)
acceleration = enviroment.compute_acceleration() # Usar para probar con Euler (metodo numerico)
# ================= BUCLE DE SIMULACION =================
# Simular mientras la particula este por encima del suelo (y ≥ 0)
while particle.position[1] >= 0:
    # Actualizar estado de la particula
    particle.update_state_rk4(0, dt)
    #particle.update_state(dt, acceleration)
    
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

# Encontrar el punto de altura máxima
altura_max = np.argmax(y_axis)
x_altura_max = x_axis[altura_max]
y_altura_max = y_axis[altura_max]

# Velocidad final
velocidad_final = np.linalg.norm(particle.velocity)

# ================= RESULTADOS EN CONSOLA =================
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
# Lineas de referencia para altura máxima
plt.axhline(y=altura_maxima, color='gray', linestyle='--', alpha=0.5, linewidth=1) # linea horizontal
plt.axvline(x=x_altura_max, color='gray', linestyle='--', alpha=0.5, linewidth=1) # linea vertical

plt.xlabel('Distancia horizontal (m)', fontsize=12, fontweight='bold') # etiqueta del eje x
plt.ylabel('Altura (m)', fontsize=12, fontweight='bold') # etiqueta del eje y
plt.title('TRAYECTORIA PARABOLICA', fontsize=14, fontweight='bold', pad=20) # titulo del grafico
plt.grid(True, alpha=0.4) # activar cuadricula
# Ajustar limites automaticamente con margen
margen_x = max(10, alcance_maximo * 0.1)
margen_y = max(10, altura_maxima * 0.1)
plt.xlim(initial_distance - margen_x, x_axis[-1] + margen_x)
plt.ylim(-5, altura_maxima + margen_y)

plt.tight_layout() # ajustar para que todo quepa
plt.show() # mostrar grafico