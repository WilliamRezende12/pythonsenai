try:
    nota1 = float(input("Digite a primeira nota: "))
    nota2 = float(input("Digite a segunda nota: "))
    nota3 = float(input("Digite a terceira nota: "))
    media = (nota1 + nota2 + nota3) / 3
    print("A média do aluno é de: ", media)

    if media >= 5:
        print("Aluno aprovado.")
    else:
        print("Aluno reprovado.")
except ValueError:
    print("Erro! Entrada de dados inválida. Informe apenas notas numéricas.")