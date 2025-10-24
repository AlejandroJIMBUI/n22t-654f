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
    """_summary_
    r = vector de posición
    q = valor de carga
    r0 = vector posición de la carga que genera el campo
    
    mag(r_vec) = magnitud de r - r0

    Returns:
        float: k x q / magnitud(r^3) x rvec
    """

# Configuración Campo Total
def campo_total(r, cargas):
    """Suma vectorial del campo eléctrico total."""
    E = vector(0, 0, 0)
    for q, pos in cargas:
        E += campo_puntual(r, q, pos)
    return E
    """_summary_
    E (0, 0, 0) = Comenzamos desde un vector nulo para ir sumando las contribuciones de cada carga
    
    Returns: 
        E += campo_puntual(r, q, pos) = El campo total es la suma vectorial de los campos individuales
    """