import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import weibull_min

lambda_weibull = 50
k_weibull = 10
pi_I = 0.4
p0 = 51

S_values = np.linspace(0, 7, 100)
pi_LB_S = 0.5 - 0.08 * S_values
pi_LS_S = 0.5 - 0.08 * S_values

x = np.linspace(25, 65, 1000)
pdf_weibull = weibull_min.pdf(x, k_weibull, scale=lambda_weibull)

def plot_weibull_distribution():
    plt.figure(figsize=(8, 5))
    plt.plot(x, pdf_weibull, label=r"Weibull Distribution $\lambda = 50$ $K = 10$", color="blue")
    plt.xlabel("Price (P)")
    plt.ylabel("Density")
    plt.title("Weibull Price Distribution")
    plt.legend()
    plt.grid()
    plt.show()

if __name__ == "__main__":
    plot_weibull_distribution()
