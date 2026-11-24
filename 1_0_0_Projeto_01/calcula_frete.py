import mod_inputs
import mod_msg
import mod_finaliza

def valida_aeroporto():
    while True:
        print("AEROPORTO DE ORIGEM: VIRACOPOS")
        print(" Digite 1 para CONGONHAS-SP - 102 KM")
        print(" Digite 2 para GUARULHOS-SP - 112 KM")
        print(" Digite 3 para CAMPO DE MARTE-SP - 98 KM")
        print(" Digite 4 para PINTO MARTINS-CE - 2922 KM")
        print(" Digite 5 para EDUARDO GOMES-AM - 6294 KM")
        print(" Digite 0 para sair\n")
        aeroporto = mod_inputs.recebe_int("Digite um número acima para escolher o aeroporto de destino: ")
        if aeroporto in ("0", "1", "2", "3", "4", "5"):
            break
        else:
            print("\nAeroporto inválido!\n")
    return aeroporto

def valida_embalagem():
    while True:
        print(" Digite 1 para Embalagem Caixa-Papelão")
        print(" Digite 2 para Embalagem Container")
        embalagem = mod_inputs.recebe_int("Digite um número acima para escolher a embalagem: ")
        if embalagem in ("1", "2"):
            break
        else:
            print("\nEmbalagem inválida!\n")
    return embalagem

def realiza_calculo_papelao():
    

def main():
    start = True
    while start:
        mod_msg.msg_cot_frete_ini()
        aeroporto = valida_aeroporto()
        embalagem = valida_embalagem()
        altura = mod_inputs.recebe_float("\nDigite a altura em metros: ")
        largura = mod_inputs.recebe_float("Digite a largura em metros: ")
        profundidade = mod_inputs.recebe_float("Digite a profundidade em metros: ")
        peso = mod_inputs.recebe_float("Digite o peso em kgs: ")
        total_itens = mod_inputs.recebe_int("Digite o total de itens: ")
        start = mod_finaliza.finaliza_programa()

if __name__ == "__main__":
    main()