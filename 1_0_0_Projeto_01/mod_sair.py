from mod_inputs import recebe_str

def finalizar():
    while True:
        try:
            opcao = recebe_str("\nDeseja finalizar o programa? Digite S para [SIM] ou N para executar outro cálculo.")
            if opcao in("S", "s") or opcao in("N", "n"):
                break
            else:
                print("Opção inválida!\n")
        except:
            print("Valor inválido!")
    if opcao in("S", "s"):
        print("\nPrograma finalizado!")
        return False
    else:
        return True