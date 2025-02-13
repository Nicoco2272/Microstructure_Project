import numpy as np
import matplotlib.pyplot as plt
from price_simulation import S_values, ILB_S, ILS_S, pi_I, p0

# Cálculo de ingresos esperados
Q = S_values  # Ingresos si todos los traders son de liquidez
R = ILB_S * S_values  # Ingresos para liquidez con la probabilidad dada
Expected_Revenue = pi_I * (ILS_S * S_values) + (1 - pi_I) * (ILB_S * S_values)

def plot_bid_ask_spread():
    """Grafica el spread Bid-Ask y los ingresos esperados."""
    plt.figure(figsize=(8, 5))
    plt.plot(S_values, Q, label='Q', color='red')
    plt.plot(S_values, R, label='R', color='blue')
    plt.plot(S_values, Expected_Revenue, label='Expected Revenue', color='green')
    plt.xlabel('Bid-Ask Spread (S)')
    plt.ylabel('Money')
    plt.title('Bid-Ask Spread')
    plt.legend()
    plt.show()

# Cálculo del óptimo de Ask y Bid
optimal_KA = p0 + max(S_values * ILB_S)
optimal_KB = p0 - max(S_values * ILS_S)

print(f'Valor óptimo de K_A (Ask): {optimal_KA}')
print(f'Valor óptimo de K_B (Bid): {optimal_KB}')

if __name__ == "__main__":
    plot_bid_ask_spread()



