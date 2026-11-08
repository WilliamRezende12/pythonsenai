nota = 0
contador = 0
soma = 0
while nota != -1:
    try:
        nota = float(input("Digite uma nota (-1 para sair): ").replace(",", "."))
        soma += nota * (nota != -1)
        contador += (nota != -1)
        resultado = soma / contador if contador > 0 else 0
    except:
        print("Valor inválido. Por favor digite apenas números.\n")
print("Valores digitados.")
print("A quantidade de notas digitadas foi de:", contador)
print("A soma das notas digitadas foi de:", soma)
print("A média do aluno é de:", resultado)