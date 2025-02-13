import numpy as np
import matplotlib.pyplot as plt
from price_simulation import S_values, pi_LB_S, pi_LS_S, pi_I, p0

# Cálculo de ingresos esperados
Q = S_values  # Ingresos si todos los traders son de liquidez
R = (1-pi_I) * S_values # Ingresos para liquidez con la probabilidad dada
Expected_Revenue = (1-pi_I) * pi_LB_S  * S_values

def plot_bid_ask_spread():
    """Grafica el spread Bid-Ask y los ingresos esperados."""
    plt.figure(figsize=(8, 5))
    plt.plot(S_values, Q, label="Todos los traders son de liquidez", color="red")
    plt.plot(S_values, R, label="Probabilidad de 40% de un trade informado", color="blue")
    plt.plot(S_values, Expected_Revenue, label="Expected Revenue", color="green")
    plt.xlabel("Bid-Ask Spread (S)")
    plt.ylabel("Money")
    plt.title("Bid-Ask Spread")
    plt.legend()
    plt.grid()
    plt.show()

if __name__ == "__main__":
    plot_bid_ask_spread()



