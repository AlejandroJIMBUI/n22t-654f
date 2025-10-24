from vpython import *
from simulation_functions import *
from field_functions import *

scene.title = "Campo Eléctrico Dinámico y Equipotenciales"
scene.width = 900
scene.height = 600
scene.background = color.black
scene.center = vector(0, 0, 0)

def dos_cargas_mismo_signo():
    scene.caption = "Dos cargas del mismo signo (campo de repulsión)"
    cargas = [(1e-6, vector(-0.6, 0, 0)), (1e-6, vector(0.6, 0, 0))]
    for q, pos in cargas:
        sphere(pos=pos, radius=0.1, color=color.cyan)
    particulas = crear_particulas([vector(-0.6, 0, 0), vector(0.6, 0, 0)])
    return cargas, particulas

def main():
    op = input(" ")
    if op == "yes":
        return dos_cargas_mismo_signo()
    elif op == "not":
        return None, None
    
cargas, particulas = main()
if cargas and particulas:
    while True:
        rate(60)
        mover_particulas(particulas, cargas)