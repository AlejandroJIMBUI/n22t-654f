from vpython import *
from src.config import *

# Configuración Campo Puntual
def campo_puntual(r, q, r0):
    """Campo eléctrico de una carga puntual."""
    r_vec = r - r0
    r_mag = mag(r_vec)
    if r_mag == 0:
        return vector(0, 0, 0)
    return (k * q / r_mag**3) * r_vec

# Configuración Campo Total
def campo_total(r, cargas):
    """Suma vectorial del campo eléctrico total."""
    E = vector(0, 0, 0)
    for q, pos in cargas:
        E += campo_puntual(r, q, pos)
    return E