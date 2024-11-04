import numpy as np
import matplotlib.pyplot as plt


lambda_servicio = 1 / 2 


def generar_tiempo_servicio(lambda_servicio):
    u = np.random.uniform(0, 1) 
    tiempo_servicio = -1 / lambda_servicio * np.log(1 - u)  
    return tiempo_servicio


tiempos_servicio = [generar_tiempo_servicio(lambda_servicio) for _ in range(100)]


print("Tiempos de servicio generados:", tiempos_servicio)


plt.hist(tiempos_servicio, bins=10, edgecolor='black', alpha=0.7)
plt.title('Distribución de Tiempos de Servicio Simulados (Exponencial)')
plt.xlabel('Tiempo de servicio (minutos)')
plt.ylabel('Frecuencia')
plt.show()