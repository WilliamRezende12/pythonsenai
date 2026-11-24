import mod_msg
import mod_inputs
import calculadora
import calcula_frete

def recebe_opcao():
    while True:
        try:
            opcao = mod_inputs.recebe_int("Digite uma opção do menu: ")
            match opcao:
                case 0:
                    print("Programa encerrado.")
                    break
                case 1:
                    #print("Calculadora. Aqui chamo a calculadora!")
                    calculadora.main()
                    break
                case 2:
                    #print("Calcular frete. Aqui chamo o calcular frete!")
                    calcula_frete.main()
                case _:
                    print("Opção inválida!\n")
        except:
            print("Erro ao receber opção!")

def main():
    while True:
        mod_msg.msg_menu_principal()
        recebe_opcao()
        break