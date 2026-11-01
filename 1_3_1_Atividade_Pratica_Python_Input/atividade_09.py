forca_g = 6.67 * 10 ** -11

massa1 = float(input("Digite a massa do primeiro corpo (kg): ").replace(",", "."))
massa2 = float(input("Digite a massa do segundo corpo (kg): ").replace(",", "."))
distancia = float(input("Digite a distância entre os corpos (m): ").replace(",", "."))

resultado = forca_g * (massa1 * massa2) / (distancia ** 2)

print("A força gravitacional entre os dois corpos é:", resultado, "N")