import pyfiglet

def msg_inicial():
    print("Seja bem-vindo ao Sistema\n")
    mensagem = pyfiglet.figlet_format("COTA-FRETE", font="pagga")
    print(mensagem)

def msg_login_ini():
    print("####################################")
    print("<<<<<<<<< LOGAR NO SISTEMA >>>>>>>>>")
    print("####################################\n")

def msg_menu_principal():
    print("############################################################")
    print("<<<<<<<<<<<<<<<<<<<<<< MENU PRINCIPAL >>>>>>>>>>>>>>>>>>>>>>")
    print("############################################################\n")
    print("##### SAIR - 0 | CALCULADORA - 1 | CALCULAR FRETE - 2 ######\n")

def msg_calc_ini():
    print("########################################################")
    print("<<<<<<<<<<<< SEJA BEM-VINDO A CALCULADORA ! >>>>>>>>>>>>")
    print("########################################################\n")

def msg_cot_frete_ini():
    print("########################################################")
    print("<<<<<<<<<<<<<<<<<< COTAÇÃO DE FRETE ! >>>>>>>>>>>>>>>>>>")
    print("########################################################\n")

def msg_final_programa():
    print("########################################################################")
    print("<<<<<<<<<<<< OBRIGADO POR UTILIZAR O PROGRAMA COTA-FRETE! >>>>>>>>>>>>>>")
    print("############################# VOLTE SEMPRE!!! ##########################\n")