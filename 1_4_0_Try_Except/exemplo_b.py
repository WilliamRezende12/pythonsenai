try:
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    resultado = num1 + num2
    print("O resultado da soma de ", num1, "+", num2, "é =", resultado)
except:
    print("Entrada de dados inválida! Digite apenas números.")