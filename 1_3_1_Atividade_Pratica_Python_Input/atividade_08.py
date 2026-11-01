espaco_inicial = float(input("Digite o espaço inicial (km): ").replace(",", "."))
espaco_final = float(input("Digite o espaço final (km): ").replace(",", "."))

tempo_inicial = float(input("Digite o tempo inicial (h): ").replace(",", "."))
tempo_final = float(input("Digite o tempo final (h): ").replace(",", "."))

resultado = (espaco_final - espaco_inicial) / (tempo_final - tempo_inicial)

print("A velocidade média do veículo foi de", resultado, "km/h.")