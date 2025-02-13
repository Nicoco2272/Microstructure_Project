import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize

def optimize_spread(p0=51, pi_I=0.4, S_range=(0, 7)):
    pi_L = 1 - pi_I

    def expected_profit(S):
        K_A = p0 + S / 2
        K_B = p0 - S / 2
        return -(pi_L * (K_A - p0) - pi_I * p0)

    opt_result = minimize(expected_profit, x0=1, bounds=[S_range])
    S_optimal = opt_result.x[0]

    K_A_opt = p0 + S_optimal / 2
    K_B_opt = p0 - S_optimal / 2

    return S_optimal, K_A_opt, K_B_opt

if __name__ == "__main__":
    S_optimal, K_A_opt, K_B_opt = optimize_spread()
    print(f"Optimal Spread: {S_optimal:.2f}")
    print(f"Optimal Ask Price (K_A): {K_A_opt:.2f}")
    print(f"Optimal Bid Price (K_B): {K_B_opt:.2f}")

