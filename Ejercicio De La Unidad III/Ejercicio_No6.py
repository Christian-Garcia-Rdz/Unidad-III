import math
import random

media = 10 
desviacion_estandar = 2 
num_clientes = 50  

mu = math.log((media ** 2) / math.sqrt(desviacion_estandar ** 2 + media ** 2))
sigma = math.sqrt(math.log(1 + (desviacion_estandar ** 2) / (media ** 2)))

tiempos_espera = [random.lognormvariate(mu, sigma) for _ in range(num_clientes)]

print("Tiempos de espera generados para cada cliente (en minutos):")
print(tiempos_espera)

frecuencia_espera = {}
for tiempo in tiempos_espera:
    tiempo_redondeado = round(tiempo)
    frecuencia_espera[tiempo_redondeado] = frecuencia_espera.get(tiempo_redondeado, 0) + 1

print("\nHistograma de tiempos de espera (Distribución Lognormal):")
for tiempo, freq in sorted(frecuencia_espera.items()):
    print(f"{tiempo} min: {'*' * freq}")

tiempo_max = max(tiempos_espera)
tiempo_min = min(tiempos_espera)
promedio_espera = sum(tiempos_espera) / len(tiempos_espera)

print("\nEstadísticas de los tiempos de espera:")
print(f"Tiempo de espera promedio: {promedio_espera:.2f} minutos")
print(f"Tiempo de espera mínimo: {tiempo_min:.2f} minutos")
print(f"Tiempo de espera máximo: {tiempo_max:.2f} minutos")

