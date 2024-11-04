import numpy as np
import matplotlib.pyplot as plt


lambda_inactividad = 1 / 10  


def generar_tiempo_inactividad(lambda_inactividad):
    u = np.random.uniform(0, 1)  
    
    tiempo_inactividad = -1 / lambda_inactividad * np.log(1 - u)  
    return tiempo_inactividad


tiempos_inactividad = [generar_tiempo_inactividad(lambda_inactividad) 
                       for _ in range(100)]


print("Tiempos de inactividad generados:", tiempos_inactividad)


plt.hist(tiempos_inactividad, bins=10, edgecolor='black', alpha=0.7)
plt.title('Distribución de Tiempos de Inactividad Simulados (Exponencial)')
plt.xlabel('Tiempo de inactividad (minutos)')
plt.ylabel('Frecuencia')
plt.show()