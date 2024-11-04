probabilidad_exito = 0.7
pedidos_diarios = 20
dias_semana = 7
resultados = []

def generar_aleatorio():
    semilla = 12345
    semilla = (semilla * 9301 + 49297) % 233280
    return semilla / 233280.0

def simular_pedidos_diarios():
    pedidos_satisfechos = 0
    for _ in range(pedidos_diarios):
        if generar_aleatorio() < probabilidad_exito:
            pedidos_satisfechos += 1
    return pedidos_satisfechos

for dia in range(dias_semana):
    pedidos_satisfechos_dia = simular_pedidos_diarios()
    resultados.append(pedidos_satisfechos_dia)

for i in range(dias_semana):
    print(f"Día {i+1}: {resultados[i]} pedidos satisfechos de {pedidos_diarios}")
