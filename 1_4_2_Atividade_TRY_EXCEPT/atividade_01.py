try:
    nome = input("Digite seu nome completo: ")
    idade = int(input("Digite sua idade em anos: "))
    print("Nome Completo: ", nome)
    print("Idade em anos: ", idade)
except ValueError:
    print("Erro! Digite uma idade válida.")