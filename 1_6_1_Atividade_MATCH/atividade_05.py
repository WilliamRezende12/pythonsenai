try:
    print("Para relatar seu problema, digite um dos números a seguir: \n")
    print("1 - Computador não liga")
    print("2 - Computador lento")
    print("3 - Problema de internet")
    print("4 - Problema de impressão.")

    problema = int(input("Digite um número para seu problema: "))
    match problema:
        case 1:
            print("Computador não liga")
            print("Verifique se o cabo de energia está conectado corretamente e se a tomada está funcionando.")
        case 2:
            print("Computador lento")
            print("Tente reiniciar o computador e verificar se há programas em execução que estejam consumindo muitos recursos.")
        case 3:
            print("Problema de internet")
            print("Verifique se o cabo de rede está conectado corretamente e se o roteador está funcionando.")
        case 4:
            print("Problema de impressão")
            print("Verifique se a impressora está conectada à rede e se há papel suficiente.")
        case _:
            print("Número inválido.")
except:
    print("Número inválido! Por favor, digite um número inteiro entre 1 e 4.")