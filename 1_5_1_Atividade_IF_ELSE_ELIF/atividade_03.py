try:
    valor = float(input("Digite o valor da compra: "))

    if valor < 0:
        print("Compra inválida.")
    elif valor <= 100:
        print("Sem desconto.")
    elif valor > 100 and valor <= 500:
        print("Desconto de 10%.")
    else:
        print("Desconto de 15%.")
except:
    print("Valor inválido. Digite apenas números.")