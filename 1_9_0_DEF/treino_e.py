def verificar_estoque(quantidade):
    if quantidade <= 5:
        return "Estoque Crítico!!!"
    elif quantidade > 5 and quantidade <= 20:
        return "Estoque baixo!"
    else:
        return "Estoque adequado."

produto = str(input("Digite o nome do produto: "))
while True:
    try:
        quantidade = float(input("Digite a quantidade em estoque: ").replace(",", "."))
        break
    except:
        print("Erro! Para quantidade, digite apenas números.")

print("O produto é:", produto)
print("A quantidade disponível em estoque é:", quantidade)
print(verificar_estoque(quantidade))