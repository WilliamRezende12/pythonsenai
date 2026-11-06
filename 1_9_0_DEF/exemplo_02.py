# Criando uma função com retorno
def calcular_media(nota1, nota2):
    media = (nota1 + nota2) / 2
    return media

# Solicitando as notas ao usuário
n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))

# Chamando a função e armazenando o retorno.
resultado = calcular_media(n1, n2)

# Exibindo o resultado.
print("A média do aluno é:", resultado)