from vpython import *
import numpy as np
from field_functions import *

# Función para la creacion de particulas
def crear_particulas(origenes, color_particula=color.orange):
    """Crea partículas en torno a las cargas."""
    particulas = []
    for origen in origenes:
        for ang in np.linspace(0, 2*np.pi, 10):
            pos = origen + vector(0.15*np.cos(ang), 0.15*np.sin(ang), 0)
            p = sphere(pos=pos, radius=0.03, color=color_particula, make_trail=True, retain=1000)
            particulas.append(p)
    return particulas
    """_summary_
    particulas = es la lista en la que se va a lamacenar la información (tuple) de las particulas.
    origen = Posición vectorial de las cargas
    for ang in np.linspace(0, 2*np.pi, 10): Crea 10 partículas distribuidas uniformemente alrededor de cada carga.
        np.linspace(0, 2*np.pi, 10): genera 10 ángulos equidistantes de 0 a 2π (círculo completo)
        
    pos = origen + vector(0.15*np.cos(ang), 0.15*np.sin(ang), 0):
        - 0.15*np.cos(ang): coordenada x relativa al origen
        - 0.15*np.sin(ang): coordenada y relativa al origen
        - 0: coordenada z (en el plano xy)
        - 0.15: radio del círculo donde se colocan las partículas
        
    formula parametrica de un circulo: 
        x = x0 + R x cos(0)
        y = y0 + R x sin(0)
        
    p = sphere(pos=pos, radius=0.03, color=color_particula, make_trail=True, retain=50):
        Crea una esfera (partícula) con propiedades específicas:
            - pos=pos: posición calculada en el círculo
            - radius=0.03: radio pequeño de la partícula
            - color=color_particula: color especificado (por defecto naranja)
            - make_trail=True: Deja un trail al moverse
            - retain=50: mantiene solo las últimas 50 posiciones del rastro
            
    Returns:
        Devuelve la lista con las particulas creadas
    """

# Funcion para configurar el movimiento de las particulas
def mover_particulas(particulas, cargas, sentido=True):
    """Mueve las partículas siguiendo las líneas del campo."""
    for p in particulas:
        E = campo_total(p.pos, cargas)
        if mag(E) != 0:
            direccion = hat(E) if sentido else -hat(E)
            p.pos += direccion * dt
    """_summary_
    E = campo_total(p.pos, cargas): Calcula el campo eléctrico TOTAL en la posición actual de la partícula
    
    if mag(E) != 0:
        - Verifica que el campo no sea cero (evita división por cero)
        - mag(E): calcula la magnitud del vector campo eléctrico
        - Si el campo es cero, la partícula no se mueve
        
    direccion = hat(E) if sentido else -hat(E): Determina la dirección del movimiento
        - hat(E): vector unitario en la dirección de E (normaliza el vector)
        - hat(E) = E / mag(E) → vector de longitud 1
        - Si sentido=True: partículas siguen la dirección del campo
        - Si sentido=False: partículas se mueven en dirección opuesta al campo
        
    p.pos += direccion * dt: Actualiza la posición de la particulas
    """