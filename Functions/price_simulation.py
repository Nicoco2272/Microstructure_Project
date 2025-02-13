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

# Cálculo de ingresos esperados
Q = S_values  # Línea de ingresos si todos los traders son de liquidez
R = ILB_S * S_values  # Línea de ingresos para liquidez con la probabilidad dada
Expected_Revenue = pi_I * (ILS_S * S_values) + (1 - pi_I) * (ILB_S * S_values)

# Gráficos
fig, axs = plt.subplots(2, 1, figsize=(8, 10))

# Gráfico de la distribución de precios
axs[0].plot(x, pdf_weibull, label=f'Weibull Distribution (λ={lambda_weibull}, K={k_weibull})', color='blue')
axs[0].set_xlabel('Price (P)')
axs[0].set_ylabel('Density')
axs[0].set_title('Weibull Price Distribution')
axs[0].legend()

# Gráfico del spread Bid-Ask
axs[1].plot(S_values, Q, label='Q', color='red')
axs[1].plot(S_values, R, label='R', color='blue')
axs[1].plot(S_values, Expected_Revenue, label='Expected Revenue', color='green')
axs[1].set_xlabel('Bid-Ask Spread (S)')
axs[1].set_ylabel('Money')
axs[1].set_title('Bid-Ask Spread')
axs[1].legend()

plt.tight_layout()
plt.show()

# Cálculo del óptimo de Ask y Bid
optimal_KA = p0 + max(S_values * ILB_S)
optimal_KB = p0 - max(S_values * ILS_S)

print(f'Valor óptimo de K_A (Ask): {optimal_KA}')
print(f'Valor óptimo de K_B (Bid): {optimal_KB}')

