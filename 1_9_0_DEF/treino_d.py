def verificar_numero(numero):
    if numero % 2 == 0:
        print("O numero", numero, "é par.")
    else:
        print("O numero", numero, "é ímpar.")
    return numero

start = True
while start:
    try:
        numero = int(input("Digite um número inteiro: "))
        break
    except:
        print("Valor inválido. Por favor, digite apenas números inteiros.")
resultado = verificar_numero(numero)