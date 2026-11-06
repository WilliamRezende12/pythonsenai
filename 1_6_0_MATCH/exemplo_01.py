try:
    nota = int(input("Digite uma nota de 1 a 5: "))
    match nota:
        case 1:
            print("Desempenho: Muito ruim!")
        case 2:
            print("Desempenho: Ruim!")
        case 3:
            print("Desempenho: Regular!")
        case 4:
            print("Desempenho: Bom!")
        case 5:
            print("Desempenho: Excelente!")
        case _:
            print("Nota inválida!")
except:
    print("Nota inválida! Por favor, digite apenas números de 1 a 5.")