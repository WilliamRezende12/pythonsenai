try:
    preco = float(input("Digite o preço do produto: "))
    desconto = float(input("Digite o percentual do desconto: "))

    valor_desconto = preco * desconto / 100
    resultado_final = preco - valor_desconto

    print("O preço final do produto após o desconto é de: ", resultado_final)

except ValueError:
    print("Erro! Entrada de dados inválida.")