import numpy as np
import matplotlib.pyplot as plt

# Dominio (longitudes de onda normalizadas)
lambdas = np.linspace(0.2, 0.8, 500)  # tipo visible (400nm - 700nm)

def planck_like(l, T=0.5):
    """Funcion de planck simplificada basada en nanometros (eje x) y
    Temperatura. 

    Args:
        l (_type_): Vector de nanometros.
        T (float, optional): Temperatura. Defaults to 0.5.

    Returns:
        _type_: Vector de intensidades.
    """
    return 1 / (l**5 * (np.exp(1/(l*T)) - 1))

# Generar curva
curve = planck_like(lambdas, T=0.5)

# Normalizar (importante para visualización)
curve = curve / np.max(curve)

# Plot
plt.figure()
plt.plot(lambdas, curve)
plt.xlabel("Longitud de onda (normalizada)")
plt.ylabel("Intensidad")
plt.title("Curva tipo Planck")
plt.grid()

# Guardar en archivo
plt.savefig("planck_curve.png", dpi=150, bbox_inches="tight")

# Cerrar figura (importante en loops)
plt.close()