# Simulación de Movimiento Parabólico

Una simulación en Python sobre lanzamiento de proyectiles. (Tiro parabólico)

## Estructura del Proyecto

| Archivo | Responsabilidad |
| :--- | :--- |
| `main.py` | Punto de entrada, gestión de inputs y orquestación de la animación. |
| `classes/particle.py` | Lógica de la partícula y algoritmos de integración (RK4). |
| `classes/enviroment.py` | Definición de constantes físicas y cálculo de aceleraciones (Gravedad + Arrastre). |

---

## Requisitos

- Python 3.8+
- Bibliotecas requeridas:
  numpy, matplotlib

---

## Ejemplo de Resultados

Al ejecutar la simulación, obtendrás métricas detalladas en la terminal y un gráfico interactivo:

* **Tiempo de vuelo** (s)
* **Alcance máximo** (m)
* **Altura máxima** (m)
* **Velocidad de impacto** (m/s)

---

## Autores

* **CarlosPimentelA** 
* **Shelaxh**
