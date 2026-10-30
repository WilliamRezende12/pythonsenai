try:
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    resultado = num1 / num2
    print("O resultado da divisão de", num1, "/", num2, "é =", resultado)
except ValueError:
    print("Entrada de dados inválida. Por favor, digite apenas números.")
except ZeroDivisionError:
    print("Erro!, não é possível dividir por zero.")