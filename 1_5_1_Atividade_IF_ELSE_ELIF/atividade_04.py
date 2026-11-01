try:
    temperatura = float(input("Digite uma temperatura: "))

    if temperatura < 0:
        print("Congelante!")
    elif temperatura >= 0 and temperatura < 15:
        print("Frio.")
    elif temperatura <= 30:
        print("Agradável.")
    else:
        print("Muito quente!")
except ValueError:
    print("Temperatura inválida. Por favor, digite um número válido para a temperatura.")