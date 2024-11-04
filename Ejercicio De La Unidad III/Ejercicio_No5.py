import numpy as np
import matplotlib.pyplot as plt
from math import comb

n = 10
p = 0.30
num_simulaciones = 100
U = np.random.uniform(0, 1, num_simulaciones)

def binomial_pmf(n, k, p):
    return comb(n, k) * (p ** k) * ((1 - p) ** (n - k))

def binomial_inverse_transform(n, p, U):
    F_k = 0
    k = 0
    while True:
        F_k += binomial_pmf(n, k, p)
        if U <= F_k:
            return k
        k += 1

compras_simuladas = [binomial_inverse_transform(n, p, u) for u in U]

print("Número de clientes que realizaron una compra en cada simulación (día):")
print(compras_simuladas)

plt.hist(compras_simuladas, bins=np.arange(min(compras_simuladas), max(compras_simuladas) + 1) - 0.5, edgecolor='black')
plt.title("Simulación de número de compras diarias (Distribución Binomial)")
plt.xlabel("Número de compras")
plt.ylabel("Frecuencia")
plt.show()
