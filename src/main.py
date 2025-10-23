from vpython import *
import numpy as np

# ----------------------------------------
# CONFIGURACIÓN DE ESCENA
# ----------------------------------------
scene.title = "Campo Eléctrico Dinámico y Equipotenciales"
scene.width = 900
scene.height = 600
scene.background = color.black
scene.center = vector(0, 0, 0)

k = 1 / (4 * np.pi * 8.8541878128e-12) # Constante de coulomb
dt = 0.01  # Paso de tiempo para animación
n_particulas = 40  # Número de partículas de prueba

# ----------------------------------------
# FUNCIONES DE CAMPO
# ----------------------------------------
def campo_puntual(r, q, r0):
    """Campo eléctrico de una carga puntual."""
    r_vec = r - r0
    r_mag = mag(r_vec)
    if r_mag == 0:
        return vector(0, 0, 0)
    return (k * q / r_mag**3) * r_vec

def campo_total(r, cargas):
    """Suma vectorial del campo eléctrico total."""
    E = vector(0, 0, 0)
    for q, pos in cargas:
        E += campo_puntual(r, q, pos)
    return E

# ----------------------------------------
# FUNCIONES DE SIMULACIÓN
# ----------------------------------------
def crear_particulas(origenes, color_particula=color.orange):
    """Crea partículas en torno a las cargas."""
    particulas = []
    for origen in origenes:
        for ang in np.linspace(0, 2*np.pi, 10):
            pos = origen + vector(0.15*np.cos(ang), 0.15*np.sin(ang), 0)
            p = sphere(pos=pos, radius=0.03, color=color_particula, make_trail=True, retain=50)
            particulas.append(p)
    return particulas

def mover_particulas(particulas, cargas, sentido=True):
    """Mueve las partículas siguiendo las líneas del campo."""
    for p in particulas:
        E = campo_total(p.pos, cargas)
        if mag(E) != 0:
            direccion = hat(E) if sentido else -hat(E)
            p.pos += direccion * dt

# ----------------------------------------
# ESCENARIOS
# ----------------------------------------
def carga_puntual():
    scene.caption = "Carga puntual aislada en movimiento de líneas de campo"
    cargas = [(1e-6, vector(0, 0, 0))]
    sphere(pos=vector(0, 0, 0), radius=0.1, color=color.cyan)
    particulas = crear_particulas([vector(0, 0, 0)])
    return cargas, particulas

def dos_cargas_mismo_signo():
    scene.caption = "Dos cargas del mismo signo (campo de repulsión)"
    cargas = [(1e-6, vector(-0.6, 0, 0)), (1e-6, vector(0.6, 0, 0))]
    for q, pos in cargas:
        sphere(pos=pos, radius=0.1, color=color.cyan)
    particulas = crear_particulas([vector(-0.6, 0, 0), vector(0.6, 0, 0)])
    return cargas, particulas

def dos_cargas_opuestas():
    scene.caption = "Dipolo eléctrico (campo entre cargas opuestas)"
    cargas = [(1e-6, vector(-0.6, 0, 0)), (-1e-6, vector(0.6, 0, 0))]
    sphere(pos=vector(-0.6, 0, 0), radius=0.1, color=color.cyan)
    sphere(pos=vector(0.6, 0, 0), radius=0.1, color=color.red)
    particulas = crear_particulas([vector(-0.6, 0, 0), vector(0.6, 0, 0)])
    return cargas, particulas

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

# ----------------------------------------
# MENÚ Y EJECUCIÓN
# ----------------------------------------
def menu():
    print("=== SIMULADOR DINÁMICO DE CAMPO ELÉCTRICO ===")
    print("1. Carga puntual aislada")
    print("2. Dos cargas del mismo signo")
    print("3. Dos cargas de signo opuesto")
    print("4. Línea de carga uniforme")

    opcion = input("Selecciona una opción (1-4): ")

    if opcion == "1":
        return carga_puntual()
    elif opcion == "2":
        return dos_cargas_mismo_signo()
    elif opcion == "3":
        return dos_cargas_opuestas()
    elif opcion == "4":
        return linea_carga_uniforme()
    else:
        print("Opción inválida.")
        return None, None

# ----------------------------------------
# BUCLE PRINCIPAL
# ----------------------------------------
cargas, particulas = menu()
if cargas and particulas:
    while True:
        rate(60)
        mover_particulas(particulas, cargas)