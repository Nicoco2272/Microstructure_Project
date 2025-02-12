import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import weibull_min

def simulate_prices(lambda_weibull=50, k_weibull=10, num_samples=10000):
    """Genera precios simulados usando la distribución Weibull."""
    prices = lambda_weibull * np.random.weibull(k_weibull, num_samples)
    return prices

def plot_price_distribution(prices):
    """Grafica la distribución de precios simulados."""
    plt.figure(figsize=(8, 5))
    plt.hist(prices, bins=50, density=True, alpha=0.6, color='b', label='Distribución Weibull')
    plt.xlabel('Precio')
    plt.ylabel('Densidad')
    plt.title('Distribución de Precios Simulados (Weibull)')
    plt.legend()
    plt.grid()
    plt.show()

if __name__ == "__main__":
    simulated_prices = simulate_prices()
    plot_price_distribution(simulated_prices)

