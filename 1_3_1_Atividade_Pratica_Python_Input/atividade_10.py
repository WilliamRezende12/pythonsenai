potencia = float(input("Digite a potência do chuveiro em watts (W): ").replace(",", "."))
tensao = float(input("Digite a tensão da rede elétrica em volts (V): ").replace(",", "."))

corrente = potencia / tensao
resultado = corrente * 1.10
print("A corrente calculada com 10 (%) de margem é:", resultado, "A")