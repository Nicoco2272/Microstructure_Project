import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import weibull_min

# Parámetros de Weibull
lambda_weibull = 50  # Escala
k_weibull = 10  # Forma

# Generar muestras de precios con distribución Weibull
np.random.seed(42)
prices = weibull_min.rvs(k_weibull, scale=lambda_weibull, size=1000)

# Valores de S en el rango de [0, 5]
S = np.linspace(0, 5, 100)

# Funciones IL_B(S) y IL_S(S)
IL_B = 0.5 - 0.08 * S
IL_S = 0.5 - 0.08 * S

# Graficar la distribución de precios simulados
plt.figure(figsize=(12, 5))

# Subgráfico 1: Histograma de precios
plt.subplot(1, 2, 1)
plt.hist(prices, bins=30, density=True, alpha=0.6, color='b', edgecolor='black')
plt.title("Distribución de Precios Weibull(λ=50, K=10)")
plt.xlabel("Precio")
plt.ylabel("Densidad")

# Subgráfico 2: IL_B(S) e IL_S(S)
plt.subplot(1, 2, 2)
plt.plot(S, IL_B, label=r"$IL_B(S) = 0.5 - 0.08S$", color='r')
plt.plot(S, IL_S, label=r"$IL_S(S) = 0.5 - 0.08S$", color='g', linestyle="dashed")
plt.title("Funciones IL_B(S) e IL_S(S)")
plt.xlabel("S")
plt.ylabel("IL Value")
plt.legend()

# Mostrar gráficos
plt.tight_layout()
plt.show()