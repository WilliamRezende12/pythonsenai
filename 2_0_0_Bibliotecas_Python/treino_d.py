from datetime import datetime

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

def calcular_entrega():
    hoje = datetime.now()
    previsao = hoje + dias_entrega()
    return previsao

quantidade = dias_entrega()
resultado = calcular_entrega()