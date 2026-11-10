from mod_inputs import inp_str

def finalizar():
    while True:
        try:
            opcao = inp_str("\nDeseja finalizar o programa? Digite S para [SIM] ou N para executar novamente o programa.")
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