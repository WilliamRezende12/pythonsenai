senha = ""
senha_correta = "12345"
while senha != senha_correta:
    try:
        senha = str(input("Digite sua senha: "))
    except:
        print("Valor inválido. Por favor digite apenas números.")
print("\nAcesso autorizado!")