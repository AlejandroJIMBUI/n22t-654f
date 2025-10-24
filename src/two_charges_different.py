from vpython import *
from simulation_functions import *
from field_functions import *

scene.title = "Campo Eléctrico Dinámico y Equipotenciales"
scene.width = 900
scene.height = 600
scene.background = color.black
scene.center = vector(0, 0, 0)

def dos_cargas_opuestas():
    scene.caption = "Dipolo eléctrico (campo entre cargas opuestas)"
    cargas = [(1e-6, vector(-0.6, 0, 0)), (-1e-6, vector(0.6, 0, 0))]
    sphere(pos=vector(-0.6, 0, 0), radius=0.1, color=color.cyan)
    sphere(pos=vector(0.6, 0, 0), radius=0.1, color=color.red)
    particulas = crear_particulas([vector(-0.6, 0, 0), vector(0.6, 0, 0)])
    return cargas, particulas

def main():
    op = input(" ")
    if op == "yes":
        return dos_cargas_opuestas()
    elif op == "not":
        return None, None
    
cargas, particulas = main()
if cargas and particulas:
    while True:
        rate(60)
        mover_particulas(particulas, cargas)