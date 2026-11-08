try:
    numero = int(input("Digite um número para ver sua tabuada: "))
    for contador in range(1, 11):
        resultado = numero * contador
        print(numero, "x", contador, "=", resultado)
except:
    print("Número inválido. Digite apenas números inteiros.")