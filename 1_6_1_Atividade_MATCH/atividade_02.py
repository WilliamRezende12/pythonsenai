try:
    dia_semana = int(input("Digite um número de 1 a 7: "))
    match dia_semana:
        case 1:
            print("Domingo!")
        case 2:
            print("Segunda-feira!")
        case 3:
            print("Terça-feira!")
        case 4:
            print("Quarta-feira!")
        case 5:
            print("Quinta-feira!")
        case 6:
            print("Sexta-feira!")
        case 7:
            print("Sábado!")
        case _:
            print("Número inválido.")
except:
    print("Número inválido! Para dias da semana, digite apenas números de 1 a 7.")