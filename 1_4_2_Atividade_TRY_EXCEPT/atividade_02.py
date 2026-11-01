try:
    num1 = float(input("Digite o primeiro número: ").replace(",", "."))
    num2 = float(input("Digite o segundo número: ").replace(",", "."))
    resultado = num1 + num2
    print("A soma de ", num1, " + ", num2, "é = ", resultado)
except ValueError:
    print("Erro! Entrada de dados inválida.")