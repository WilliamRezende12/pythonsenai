contador = 1
soma = 0
while contador <= 5:
    try:
        numero = int(input("Digite um número: "))
        soma += numero
        contador += 1
    except:
        print("Número inválido.")
print("A soma total dos números é:", soma)