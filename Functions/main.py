import price_simulation
import expected_revenue
import bid_ask_optimization

if __name__ == "__main__":
    print("Ejecutando simulación de precios")
    price_simulation.plot_weibull_distribution()

    print("Calculando ingresos esperados y graficando spread Bid-Ask")
    expected_revenue.plot_bid_ask_spread()

    print("Optimizando Bid-Ask Spread")
    S_optimal, K_A_opt, K_B_opt = bid_ask_optimization.optimize_spread()
    print(f"Optimal Spread: {S_optimal:.2f}")
    print(f"Optimal Ask Price (K_A): {K_A_opt:.2f}")
    print(f"Optimal Bid Price (K_B): {K_B_opt:.2f}")





