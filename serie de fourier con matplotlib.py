import numpy as np
import matplotlib.pyplot as plt

# Definir la función discontinua (periódica)
def funcion_discontinua(t):
    return np.where((t >= 0) & (t < np.pi), 1, -1)

# Serie de Fourier truncada
def serie_fourier(func, T, N, t):
    """
    Aproxima una función discontinua mediante su serie de Fourier truncada.
    
    Args:
    func: Función discontinua
    T: Periodo de la función
    N: Número de términos en la serie de Fourier
    t: Puntos de tiempo donde evaluar la serie
    
    Regresa:
    Aproximación de la serie de Fourier en los puntos t.
    """
    a0 = (1 / T) * np.trapz(func(np.linspace(-T / 2, T / 2, 1000)), np.linspace(-T / 2, T / 2, 1000))
    series_sum = np.ones_like(t) * a0  # Componente constante

    for n in range(1, N + 1):
        # Coeficientes an y bn
        an = (2 / T) * np.trapz(
            func(np.linspace(-T / 2, T / 2, 1000)) * np.cos(2 * np.pi * n * np.linspace(-T / 2, T / 2, 1000) / T),
            np.linspace(-T / 2, T / 2, 1000),
        )
        bn = (2 / T) * np.trapz(
            func(np.linspace(-T / 2, T / 2, 1000)) * np.sin(2 * np.pi * n * np.linspace(-T / 2, T / 2, 1000) / T),
            np.linspace(-T / 2, T / 2, 1000),
        )

        # Construir la suma de la serie
        series_sum += an * np.cos(2 * np.pi * n * t / T) + bn * np.sin(2 * np.pi * n * t / T)

    return series_sum

# Parámetros
T = 2 * np.pi  # Periodo
t = np.linspace(-3 * np.pi, 3 * np.pi, 1000)  # Intervalo extendido para ver periodicidad
N = 10  # Reducir el número de términos

# Generar la función y su aproximación
func = funcion_discontinua(t % T - np.pi)
f_serie = serie_fourier(funcion_discontinua, T, N, t % T - np.pi)

# Graficar
plt.figure(figsize=(8, 5))
plt.plot(t, f_serie, label="Serie de Fourier", color="green")
plt.axhline(0, color="black", linewidth=0.5)  # Línea del eje x
plt.axvline(0, color="black", linewidth=0.5)  # Línea del eje y
plt.title("Aproximación de Fourier de una función discontinua")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.grid(True)
plt.show()

