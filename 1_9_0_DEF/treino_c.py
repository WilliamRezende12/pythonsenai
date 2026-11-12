def calcular_desconto(preco_produto, perc_desconto):
    desconto = preco_produto * perc_desconto / 100
    preco_final = preco_produto - desconto

    return preco_final

def receber_numero(mensagem):
    start = True
    while start:
        try:
            numero = float(input(mensagem).replace(",", "."))
            start = False
        except:
            print("Valor inválido! Por favor, digite apenas números.")
    return numero

preco_produto = receber_numero("Digite o preço do produto: ")
percentual_desconto = receber_numero("Digite o percentual de desconto: ")
resultado = calcular_desconto(preco_produto, percentual_desconto)

print("\nO preço do produto é de:", preco_produto)
print("A porcentagem de desconto é de:", percentual_desconto,"%")
print("O valor final do produto é de:", resultado)