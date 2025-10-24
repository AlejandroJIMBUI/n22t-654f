from vpython import *
import numpy as np
from simulation_functions import *
from field_functions import *

scene.title = "Campo Eléctrico Dinámico y Equipotenciales"
scene.width = 900
scene.height = 600
scene.background = color.black
scene.center = vector(0, 0, 0)

def linea_carga_uniforme():
    scene.caption = "Línea de carga uniforme (campo extendido)"
    cargas = []
    origenes = []
    for i in np.linspace(-1, 1, 10):
        cargas.append((1e-7, vector(i, 0, 0)))
        sphere(pos=vector(i, 0, 0), radius=0.05, color=color.cyan)
        origenes.append(vector(i, 0, 0))
    particulas = crear_particulas(origenes)
    return cargas, particulas

def main():
    op = input(" ")
    if op == "yes":
        return linea_carga_uniforme()
    elif op == "not":
        return None, None
    
cargas, particulas = main()
if cargas and particulas:
    while True:
        rate(60)
        mover_particulas(particulas, cargas)