try:
    saldo_bancario_inicial = 1000

    print("Bem-vindo ao menu bancário!")
    print("Digite uma das opções a seguir: \n")
    print("Para consultar o saldo, digite 1.")
    print("Para depositar, digite 2.")
    print("Para sacar, digite 3.")
    print("Para sair, digite 4.")

    numero = int(input("Digite: "))
    match numero:
        case 1:
            print("Seu saldo bancário inicial é de ", saldo_bancario_inicial)
        case 2:
            print("Depositar")
        case 3:
            print("Sacar")
        case 4:
            print("Sair")
        case _:
            print("Número inválido.")
except:
    print("Número inválido! Por favor, digite um número inteiro de 1 a 4.")