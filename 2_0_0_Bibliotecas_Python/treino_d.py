import datetime

def dias_entrega(mensagem):
    while True:
        try:
            dia = int(input(mensagem))
            break
        except:
            print("Valor inválido. Por favor digite apenas números inteiros.")
    return dia