def calcular_media(n1, n2, n3):
    media = (n1 + n2 + n3) / 3
    
    return media

def receber_numero(mensagem):
    start = True
    while start:
        try:
            nota = float(input(mensagem).replace(",", "."))
            start = False
        except:
            print("Nota inválida. Por favor digite apenas números.")
    return nota

print("Digite apenas notas de 0 a 10\n")

nota1 = receber_numero("Digite a primeira nota: ")
nota2 = receber_numero("Digite a segunda nota: ")
nota3 = receber_numero("Digite a terceira nota: ")

resultado = calcular_media(nota1, nota2, nota3)
print("A média do aluno é:", resultado)

resultado_media = resultado
if resultado_media >= 5:
    print("Aluno aprovado!")
else:
    print("Aluno reprovado!")