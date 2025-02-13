import price_simulation
import expected_revenue

if __name__ == "__main__":
    print("Ejecutando simulación de precios...")
    price_simulation.plot_weibull_distribution()

    print("Calculando ingresos esperados y graficando spread Bid-Ask...")
    expected_revenue.plot_bid_ask_spread()

    print(f'Valor óptimo de K_A (Ask): {expected_revenue.optimal_KA}')
    print(f'Valor óptimo de K_B (Bid): {expected_revenue.optimal_KB}')





