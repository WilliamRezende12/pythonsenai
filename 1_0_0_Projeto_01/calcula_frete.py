import mod_msg
import mod_inputs
import mod_finaliza

def recebe_opcao():
    while True:
        mod_msg.msg_ct_aeroporto()
        opcao = mod_inputs.recebe_int("Digite uma opção: ")
        if opcao in(0, 1, 2, 3, 4, 5):
            break
        else:
            print("Opção inválida!\n")
    return opcao

def escolhe_aeroporto(opcao):
    aeroporto = ["CONGONHAS/SP", "GUARULHOS/SP", "CAMPO DE MARTE/SP", "PINTO MARTINS/CE", "EDUARDO GOMES/AM"]
    return aeroporto[opcao-1]

def escolhe_distancia(opcao):
    distancia = [102, 112, 98, 2922, 6294]
    return distancia[opcao-1]

def recebe_embalagem():
    while True:
            mod_msg.msg_embalagem()
            opcao = mod_inputs.recebe_int("Digite uma opção de embalagem: ")
            if opcao in(0, 1, 2):
                break
            else:
                print("Opção inválida!\n")
    return opcao

def tipo_emb(tipo_embalagem):
    match tipo_embalagem:
        case 1:
            embalagem = "Caixa de Papelão"
        case 2:
            embalagem = "Caixa Container"
    return embalagem

def recebe_altura():
    while True:
        try:
            altura = mod_inputs.recebe_float("Digite a altura do item em mts: ".replace(",", "."))
            break
        except:
            print("Altura inválida!")
    return altura

def recebe_largura():
    while True:
        try:
            largura = mod_inputs.recebe_float("Digite a largura do item em mts: ".replace(",", "."))
            break
        except:
            print("Largura inválida!")
    return largura

def recebe_profundidade():
    while True:
        try:
            profundidade = mod_inputs.recebe_float("Digite a profundidade do item em mts: ".replace(",", "."))
            break
        except:
            print("Profundidade inválida!")
    return profundidade

def recebe_peso():
    while True:
        try:
            peso = mod_inputs.recebe_float("Digite o peso do item em kgs: ".replace(",", "."))
            break
        except:
            print("Peso inválido!")
    return peso

def recebe_total_itens():
    while True:
        try:
            total = mod_inputs.recebe_int("Digite o total de itens: ")
            break
        except:
            print("Valor inválido!")
    return total

def calculo_frete(distancia, tipo_embalagem):
    match tipo_embalagem:
        case 1:
            y = recebe_altura()
            x = recebe_largura()
            z = recebe_profundidade()
            w = recebe_peso()
            f = 0.26
        case 2:
            y = recebe_altura()
            x = recebe_largura()
            z = recebe_profundidade()
            w = recebe_peso()
            f = 0.37
    formula = ((y * x * z * w) * (1 + f)) * (1 + (distancia * 9.8))
    return formula

def main():
    start = True
    while start:
        opcao = recebe_opcao()
        if opcao != 0:
            aeroporto = escolhe_aeroporto(opcao)
            distancia = escolhe_distancia(opcao)
            tipo_embalagem = recebe_embalagem()
            embalagem = tipo_emb(tipo_embalagem)
            valor_frete = calculo_frete(distancia, tipo_embalagem)
            total_itens = recebe_total_itens()
            resultado = valor_frete * total_itens
            print("O aeroporto é: ", aeroporto)
            print("A distância é: ", distancia, "Km")
            print("O tipo de embalagem é: ", embalagem)
            print("O total de itens é: ", total_itens)
            print("O valor do frete é: RS", round(resultado, 2))
            start = mod_finaliza.finaliza_programa()
        else:
            break

if __name__ == "__main__":
    main()