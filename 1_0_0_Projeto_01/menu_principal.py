import mod_msg
import mod_inputs
import mod_calculadora

def recebe_opcao():
    while True:
        try:
            opcao = mod_inputs.recebe_int("Digite uma opção do menu: ")
            match opcao:
                case 0:
                    print("Programa encerrado.")
                case 1:
                    print("Calculadora. Aqui chamo a calculadora!")
                    mod_calculadora.main()
                case 2:
                    print("Calcular frete. Aqui chamo o calcular frete!")
                case _:
                    print("Opção inválida!\n")
        except:
            print("Erro ao receber opção!")

def main():
    mod_msg.msg_menu_principal()
    recebe_opcao()