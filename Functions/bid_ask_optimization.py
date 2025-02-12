import numpy as np
import matplotlib.pyplot as plt

def copeland_galai_optimization(p_0, pi_i, pi_l_b=0.5, pi_l_s=0.5, s_range=np.linspace(0, 0.5, 100)):
    """Calcula el bid/ask óptimo basado en el modelo de Copeland & Galai."""
    pi_l_b_s = np.clip(pi_l_b - 0.085 * s_range, 0, 0.5)
    pi_l_s_s = np.clip(pi_l_s - 0.085 * s_range, 0, 0.5)
    bid = p_0 * (1 - (1 - pi_i) * pi_l_b_s)
    ask = p_0 * (1 + (1 - pi_i) * pi_l_s_s)
    spread = ask - bid
    return s_range, bid, ask, spread

if __name__ == "__main__":
    # Llamada a la función para obtener los resultados
    s_values, bid_values, ask_values, spread_values = copeland_galai_optimization(p_0=51, pi_i=0.4)

    # Imprimir resultados
    print("Valores S:", s_values)
    print("Bid:", bid_values)
    print("Ask:", ask_values)
    print("Spread:", spread_values)

    # Crear la gráfica
    plt.figure(figsize=(10, 6))
    plt.plot(s_values, bid_values, label='Bid', color='blue')
    plt.plot(s_values, ask_values, label='Ask', color='red')
    plt.plot(s_values, spread_values, label='Spread', color='green')

    # Añadir etiquetas y título
    plt.title('Bid/Ask Optimization: Copeland & Galai Model')
    plt.xlabel('S Range')
    plt.ylabel('Price')
    plt.legend()

    # Mostrar la gráfica
    plt.grid(True)
    plt.show()
