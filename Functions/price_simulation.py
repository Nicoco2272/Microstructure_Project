import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import weibull_min


def simulate_prices(lambda_weibull=50, k_weibull=10, num_samples=10000):
    """Genera precios simulados usando la distribución Weibull."""
    prices = lambda_weibull * np.random.weibull(k_weibull, num_samples)
    return prices


def plot_price_distribution(prices):
    """Grafica la distribución de precios simulados en forma de línea."""
    # Crear un rango de valores para los precios
    price_range = np.linspace(min(prices), max(prices), 1000)

    # Obtener la densidad de probabilidad usando la función de densidad de la distribución Weibull
    pdf_values = weibull_min.pdf(price_range, 10, scale=50)

    plt.figure(figsize=(8, 5))
    plt.plot(price_range, pdf_values, color='b', label=r"Distribución Weibull $\lambda = 50$, $K = 10$")
    plt.xlabel("Precio")
    plt.ylabel("Densidad")
    plt.title("Distribución de Precios Simulados (Weibull)")
    plt.legend()
    plt.grid()
    plt.show()


if __name__ == "__main__":
    simulated_prices = simulate_prices()
    plot_price_distribution(simulated_prices)

