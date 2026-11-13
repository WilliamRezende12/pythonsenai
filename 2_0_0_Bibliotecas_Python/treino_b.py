import math

def receber_numero(mensagem):
    while True:
        try:
            num1 = float(input(mensagem).replace(",","."))
            break
        except:
            print("Valor inválido. Digite apenas números.\n")
    return num1 

def raiz(num1):
    resultado = math.sqrt(num1)
    return resultado

def potencia(num1, num2):
    resultado = math.pow(num1, num2)
    return resultado
 
num1 = receber_numero("\nDigite o primeiro número: ")
num2 = receber_numero("\nDigite o segundo número: ")
raiz_quadrada = raiz(num1)
pot = potencia(num1, num2)

print("Primeiro número:", num1)
print("\nSegundo número:", num2)
print("\nRaiz quadrada:", raiz_quadrada)
print("\nPotência:", pot)