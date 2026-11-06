try:
    print("Digite um número de 1 a 4 para seguir com as opções do menu bancário: ")
    print("Para consultar o saldo, digite 1")
    print("Para depositar, digite 2")
    print("Para sacar, digite 3")
    print("Para sair, digite 4")
except:
    print("Número inválido.")

    saldo_bancario_inicial = 1000
    menu_bancario = int(input("Digite um número de 1 a 4 para seguir com as opções do menu bancário: "))
except:
    print("Número inválido. Para consultar o menu bancário, digite apenas números de 1 a 4.")
    
try:
    print("Digite um número de 1 a 4 para seguir com as opções do menu bancário: ")
    print("Para consultar o saldo, digite 1")
    print("Para depositar, digite 2")
    print("Para sacar, digite 3")
    print("Para sair, digite 4")
except:
    print("Número inválido.")

match menu_bancario:
        case 1:
            print("Consultar saldo")
            print("Saldo bancário inicial é de ", saldo_bancario_inicial)
        case 2:
            print("Depositar")
        case 3:
            print("Sacar")
        case 4:
            print("Sair")
        case _:
            print("Número inválido!")