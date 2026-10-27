# Recebendo dados usando input

# Receber o nome do usuário:
nome = str(input("Digite seu nome completo: "))

# Receber a idade do usuário:
idade = int(input("Digite sua idade em anos: "))

# Receber o peso do usuário:
# Professor utilizou o replace para resolver a troca de , por .
peso = float(input("Digite seu peso em kg: ").replace(",", "."))

# Visualizar o nome digitado
print("O nome do usuário é:", nome)
print("A idade do usuário é:", idade, "anos")
print("O peso do usuário é:", str(peso).replace(".", ","), "kg")