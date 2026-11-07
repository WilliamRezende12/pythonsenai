try:
    print("Para calcular o desconto, selecione a categoria do produto: \n")
    print("1 - Informática")
    print("2 - Eletrônicos")
    print("3 - Acessórios")

    categoria = int(input("Digite um número para categoria : "))
    match categoria:
        case 1:
            print("Informática - Desconto de 10%")
        case 2:
            print("Eletrônicos - Desconto de 5%")
        case 3:
            print("Acessórios - Desconto de 2%")
        case _:
            print("Número inválido.")
except:
    print("Número inválido! Por favor, digite um número inteiro entre 1 e 3.")