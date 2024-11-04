import random
from math import comb

n = 10
p = 0.30
num_simulaciones = 100
U = [random.uniform(0, 1) for _ in range(num_simulaciones)]

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

# Crear histograma manualmente
frecuencia = {}
for compra in compras_simuladas:
    if compra in frecuencia:
        frecuencia[compra] += 1
    else:
        frecuencia[compra] = 1

print("\nHistograma de número de compras diarias:")
for compra, freq in sorted(frecuencia.items()):
    print(f"{compra}: {'*' * freq}")
