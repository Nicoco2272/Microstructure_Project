from Functions.price_simulation import simulate_prices, plot_price_distribution
from Functions.expected_revenue import expected_revenue, plot_expected_revenue

# Simulación de precios
prices = simulate_prices()
plot_price_distribution(prices)

# Cálculo y visualización del ingreso esperado
s_values, revenue_values = expected_revenue(pi_i=0.4)
plot_expected_revenue(s_values, revenue_values)


