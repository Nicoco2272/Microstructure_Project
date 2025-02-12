import numpy as np
import matplotlib.pyplot as plt

def expected_revenue(pi_i, pi_l_b=0.5, pi_l_s=0.5, s_range=np.linspace(0, 0.5, 100)):
    """Calcula el ingreso esperado en función de los parámetros dados."""
    pi_l_b_s = np.clip(pi_l_b - 0.085 * s_range, 0, 0.5)
    pi_l_s_s = np.clip(pi_l_s - 0.085 * s_range, 0, 0.5)
    revenue = (1 - pi_i) * (pi_l_b_s + pi_l_s_s)
    return s_range, revenue

def plot_expected_revenue(s_range, revenue):
    """Grafica el ingreso esperado en función de S."""
    plt.figure(figsize=(8, 5))
    plt.plot(s_range, revenue, label='Ingreso Esperado', color='r')
    plt.xlabel('S')
    plt.ylabel('Ingreso Esperado')
    plt.title('Ingreso Esperado vs. S')
    plt.legend()
    plt.grid()
    plt.show()

if __name__ == "__main__":
    s_values, revenue_values = expected_revenue(pi_i=0.4)
    plot_expected_revenue(s_values, revenue_values)