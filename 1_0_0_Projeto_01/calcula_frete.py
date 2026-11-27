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

def escolha_embalagem(opcao):
    embalagem = ["Embalagem Caixa Papelão", "Embalagem Container"]
    return embalagem[opcao-1]

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


def main():
    start = True
    while start:
        opcao = recebe_opcao()
        if opcao != 0:
            aeroporto = escolhe_aeroporto(opcao)
            distancia = escolhe_distancia(opcao)
            print("O aeroporto é: ", aeroporto)
            print("A distância é: ", distancia)
        else:
            break

        embalagem = recebe_embalagem()
        if embalagem != 0:
            embalagem = escolha_embalagem(embalagem)
            print("A embalagem é: ", embalagem)
        else:
            break

        # Realizando cálculo PAPELÃO
        altura = recebe_altura()
        largura = recebe_largura()
        profundidade = recebe_profundidade()
        peso = recebe_peso()
        total_itens = recebe_total_itens()
        custo_operacional_papelao = 0.26
        distancia_km = escolhe_distancia(opcao)

        resultado = ((altura * largura * profundidade * peso) * (1 + custo_operacional_papelao)) * (1 + (distancia_km * 9.8))
        print("\nA distância é de: ", distancia_km, "Km")
        print("\nA altura do item é de: ", altura, "Mts")
        print("\nA largura do item é de: ", largura, "Mts")
        print("\nA profundidade do item é de: ", profundidade, "Mts")
        print("\nO peso do item é de: ", peso, "Kg")
        print("\nO total de itens é de: ", total_itens, "itens")
        print("\nA altura do item é de: ", altura, "Mts")
        print("\nO resultado do cálculo para embalagem de papelão é = ", resultado)

        # Realizando cálculo CONTAINER
        altura = recebe_altura()
        largura = recebe_largura()
        profundidade = recebe_profundidade()
        peso = recebe_peso()
        total_itens = recebe_total_itens()
        custo_operacional_container = 0.37
        distancia_km = escolhe_distancia(opcao)

        resultado = ((altura * largura * profundidade * peso) * (1 + custo_operacional_container)) * (1 + (distancia_km * 9.8))
        print("\nA distância é de: ", distancia_km, "Km")
        print("\nA altura do item é de: ", altura, "Mts")
        print("\nA largura do item é de: ", largura, "Mts")
        print("\nA profundidade do item é de: ", profundidade, "Mts")
        print("\nO peso do item é de: ", peso, "Kg")
        print("\nO total de itens é de: ", total_itens, "itens")
        print("\nA altura do item é de: ", altura, "Mts")
        print("\nO resultado do cálculo para embalagem de container é = ", resultado)

        # Realizando cálculo CONTAINER
        altura = recebe_altura()
        largura = recebe_largura()
        profundidade = recebe_profundidade()
        peso = recebe_peso()
        total_itens = recebe_total_itens()
        custo_operacional_container = 0.37
        distancia_km = escolhe_distancia(opcao)

        resultado = ((altura * largura * profundidade * peso) * (1 + custo_operacional_container)) * (1 + (distancia_km * 9.8))
        print("\nA distância é de: ", distancia_km, "Km")
        print("\nA altura do item é de: ", altura, "Mts")
        print("\nA largura do item é de: ", largura, "Mts")
        print("\nA profundidade do item é de: ", profundidade, "Mts")
        print("\nO peso do item é de: ", peso, "Kg")
        print("\nO total de itens é de: ", total_itens, "itens")
        print("\nA altura do item é de: ", altura, "Mts")
        print("\nO resultado do cálculo para embalagem de container é = ", resultado)

        start = mod_finaliza.finaliza_programa()

if __name__ == "__main__":
    main()