def soma(num1, num2):
    soma = num1 + num2
    return soma

start = True
while start:
    try:
        num1 = float(input("Digite seu primeiro número:").replace(",", "."))
        start = False
    except:
        print("Valor inválido! Por favor, digite apenas números.")

start = True
while start:
    try:
        num2 = float(input("Digite seu segundo número:").replace(",", "."))
        start = False
    except:
        print("Valor inválido! Por favor, digite apenas números.")
resultado = soma(num1, num2)
print("O valor da soma é:", resultado)