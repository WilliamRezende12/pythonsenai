soma = 0
try:
    for contador in range(1, 6):
        numero = int(input("Digite um número inteiro: "))
        soma += numero
    print("A soma dos números digitados é:", soma)
except:
    print("Número inválido. Digite apenas números inteiros.")