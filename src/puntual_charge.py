from vpython import *
from simulation_functions import *

scene.title = "Campo Eléctrico Dinámico y Equipotenciales"
scene.width = 900
scene.height = 600
scene.background = color.black
scene.center = vector(0, 0, 0)


def carga_puntual():
    scene.caption = "Carga puntual aislada en movimiento de líneas de campo"
    cargas = [(1e-6, vector(0, 0, 0))]
    sphere(pos=vector(0, 0, 0), radius=0.1, color=color.cyan)
    particulas = crear_particulas([vector(0, 0, 0)])
    return cargas, particulas

def main():
    op = input(" ")
    if op == "yes":
        return carga_puntual()
    elif op == "not":
        return None, None
    
cargas, particulas = main()
if cargas and particulas:
    while True:
        rate(60)
        mover_particulas(particulas, cargas)