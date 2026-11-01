try:
    idade = int(input("Digite sua idade em anos: "))
    if idade <= 0:
        print("Idade inválida.")
    elif idade > 0 and idade <= 12:
        print("Você é uma criança")
    elif idade > 12 and idade < 18:
        print("Você é um adolescente.")
    elif idade >= 18:
        print("Você é um adulto.")
except:
    print("Idade inválida. Digite apenas um número.")