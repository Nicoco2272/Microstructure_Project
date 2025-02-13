import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import weibull_min

# Parámetros del modelo
lambda_weibull = 50  # Parámetro de escala
k_weibull = 10  # Parámetro de forma
pi_I = 0.4  # Probabilidad de una operación informada
p0 = 51  # Precio inicial

# Funciones de probabilidad para los traders de liquidez
S_values = np.linspace(0, 7, 100)
ILB_S = 0.5 - 0.08 * S_values
ILS_S = 0.5 - 0.08 * S_values

# Distribución de precios de la Weibull
x = np.linspace(25, 65, 1000)
pdf_weibull = weibull_min.pdf(x, k_weibull, scale=lambda_weibull)

def plot_weibull_distribution():
    """Grafica la distribución de precios Weibull."""
    plt.figure(figsize=(8, 5))
    plt.plot(x, pdf_weibull, label=f'Weibull Distribution (λ={lambda_weibull}, K={k_weibull})', color='blue')
    plt.xlabel('Price (P)')
    plt.ylabel('Density')
    plt.title('Weibull Price Distribution')
    plt.legend()
    plt.show()

if __name__ == "__main__":
    plot_weibull_distribution()
