import math

def recebe_numero():
    while True:
        try:
            numero = float(input("Digite o raio da mesa em metros: ").replace(",", "."))
            break
        except:
            print("Valor inválido. Digite apenas um número.")
    return numero

def calcula_area(raio):
    area = math.pi * math.pow(raio, 2)
    return area

raio = recebe_numero()
area = round(calcula_area(raio), 2) # Round arredonda para 2 casas decimais.

print("A área da mesa é: ", area, "Mt2")