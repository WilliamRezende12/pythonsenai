try:
    num1 = float(input("Digite o primeiro número: ").replace(",", "."))
except:
    print("Valor inválido para o primeiro número!")

try:
    num2 = float(input("Digite o segundo número: ").replace(",", "."))
except:
    print("Valor inválido para o segundo número!")

try:
    print("Digite uma das operações a seguir: \n")
    print("Para Multiplicação, digite *")
    print("Para Divisão, digite /")
    print("Para Adição, digite +")
    print("Para Subtração, digite -")
    operador = str(input("Digite uma operação acima: "))
except:
    print("Operador inválido")

match operador:
    case "*":
        resultado = num1 * num2
        print("O resultado de ", num1, operador, num2, "é = ", resultado)
    case "/":
        resultado = num1 / num2
        print("O resultado de ", num1, operador, num2, "é = ", resultado)
    case "+":
        resultado = num1 + num2
        print("O resultado de ", num1, operador, num2, "é = ", resultado)
    case "-":
        resultado = num1 - num2
        print("O resultado de ", num1, operador, num2, "é = ", resultado)
    case _:
        print("Operador inválido!")