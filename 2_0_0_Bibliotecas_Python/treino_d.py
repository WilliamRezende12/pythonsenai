import datetime

def dias_entrega():
    start = True
    while start:
        try:
            dia = int(input("Digite a quantidade de dias para entrega: "))
            if dia < 0:
                print("Erro! O dia precisa ser positivo!")
            else:
                start = False
        except:
            print("Valor inválido. Por favor digite apenas números inteiros.")
    return dia

def calcular_entrega(dia):
    hoje = datetime.date.today()
    previsao = hoje + datetime.timedelta(days=dia)
    return previsao

quantidade = dias_entrega()
resultado = calcular_entrega(quantidade)

print("\nData atual:", datetime.date.today().strftime("%d/%m/%Y"))
print("\nDias para entrega:", quantidade)
print("\nPrevisão de entrega:", resultado.strftime("%d/%m/%Y"))