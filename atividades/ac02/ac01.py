def ajustar_temperatura(temperatura_atual):
    temperatura_desejada = float(input("Defina a temperatura desejada: "))

    if temperatura_desejada > temperatura_atual:
        print("Aquecendo... Temperatura ajustada para " + str(temperatura_desejada) + "°C.")
    elif temperatura_desejada < temperatura_atual:
        print("Resfriando... Temperatura ajustada para " + str(temperatura_desejada) + "°C.")
    else:
        print("A temperatura já está ideal.")
    return temperatura_desejada


def verificar_consumo(temperatura, consumo):
    if temperatura < 18 or temperatura > 26:
        consumo += 10
        print("Consumo elevado! Atual: " + str(consumo) + "kWh.")
    else:
        consumo -= 5 if consumo > 0 else 0
        print("Consumo otimizado. Atual: " + str(consumo) + "kWh.")
    return consumo


consumo = float(input("Informe o consumo atual de energia (kWh): "))
temperatura_atual = float(input("Informe a temperatura atual (°C): "))

saldo_energia = verificar_consumo(temperatura_atual, consumo)

while True:
    print("Deseja ajustar a temperatura?")
    resposta = input("Sim ou Não? ").upper()

    if resposta == "SIM":
        temperatura_atual = ajustar_temperatura(temperatura_atual)
        saldo_energia = verificar_consumo(temperatura_atual, saldo_energia)
    elif resposta == "NÃO":
        print("Sistema finalizado. Temperatura estável e consumo monitorado.")
        break