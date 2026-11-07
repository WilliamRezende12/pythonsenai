opcao = 1
print("Menu de opções:")
print("1 - Cadastro")
print("2 - Consulta")
print("3 - Relatório")
print("4 - Sair")
while opcao != 4:
    try:
        opcao = int(input("Digite um número de 1 a 4: "))
        match opcao:
            case 1:
                print("Cadastro.")
            case 2:
                print("Consulta.")
            case 3:
                print("Relatório.")
            case 4:
                print("Sair.")
            case _:
                print("Opção inválida! Digite de 1 a 4.")
    except:
        print("Entrada inválida! Digite apenas números.")