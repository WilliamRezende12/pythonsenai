from datetime import datetime

def receber_data():
    start = True
    while start:
        try:
            data = str(input("Digite sua data de nascimento: "))
            data_nasc = datetime.strptime(data, "%d/%m/%Y")
            if data_nasc.date() > datetime.now().date():
                print("Erro: A data de nascimento não pode ser futura!\n")
            else:
                start = False
        except:
            print("Data inválida! Por favor, digite uma data no formato DD/MM/AAAA\n")
    return data_nasc

def verifica_aniversario(data_nascimento):
    data_atual = datetime.now()

    if (data_atual.month, data_atual.day) >= (data_nascimento.month, data_nascimento.day):
        mensagem = "Você já fez aniversário neste ano!"
    else:
        mensagem = "Você ainda não fez aniversário neste ano!"
    return mensagem
    
data_niver = receber_data()
verifica_niver = verifica_aniversario(data_niver)
print("Sua data de aniversário é:", data_niver.strftime("%d/%m/%Y"))
print(verifica_aniversario(data_niver))