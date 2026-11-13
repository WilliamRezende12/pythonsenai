import datetime

def receber_nascimento(mensagem):
    while True:
        try:
            data = int(input(mensagem))
            break
        except:
            print("Valor inválido. Por favor digite apenas números inteiros.")
    return data

dia = receber_nascimento("Digite o dia em que nasceu: ")
mes = receber_nascimento("Digite o mês em que nasceu: ")
ano = receber_nascimento("Digite o ano em que nasceu: ")
agora = datetime.now()

print("Data de nascimento:",dia, mes, ano )
print("Data atual", agora)
print("Resultado:")