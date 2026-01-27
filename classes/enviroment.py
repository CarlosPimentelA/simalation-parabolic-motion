import numpy as np

class Environment:
    def __init__(self, gravity, air_density=1.225, drag_coefficient=0.47, cross_sectional_area=0.05):
        self.gravity = gravity
        self.air_density = air_density      # Densidad del aire
        self.drag_coefficient = drag_coefficient  # "Como de aerodinamico es el objeto"
        self.cross_sectional_area = cross_sectional_area  # Area que "ve" el aire (m²)
        
    def compute_acceleration(self, velocity):
        gravity_acc = np.array([0, -self.gravity])
        
        # Solo si hay movimiento
        if np.linalg.norm(velocity) > 0:
            # FORMULA DE RESISTENCIA DEL AIRE:
            # F_drag = -0.5 * ρ * C_d * A * v² * (vector direccion)
            # donde:
            #   ρ = densidad del aire (air_density)
            #   C_d = coeficiente de arrastre (drag_coefficient)
            #   A = area transversal (cross_sectional_area)
            #   v = magnitud de la velocidad (norma)
            #   (v/|v|) = vector unitario en direccion de la velocidad

            # Cálculo de la fuerza de arrastre
            drag_force = -0.5 * self.air_density * self.drag_coefficient * \
                        self.cross_sectional_area * np.linalg.norm(velocity) * velocity

            # La fuerza de arrastre se convierte en aceleracion
            drag_acc = drag_force
        else:
            # Si no hay velocidad, no hay resistencia del aire
            drag_acc = np.array([0.0, 0.0])
            
        # 3. SUMA DE ACELERACIONES:
        # Aceleracion total = gravedad + resistencia del aire
        return gravity_acc + drag_acc