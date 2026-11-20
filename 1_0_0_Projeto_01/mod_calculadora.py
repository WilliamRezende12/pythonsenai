import mod_msg
import mod_inputs
import mod_sair

def valida_operador():
    while True:
        print(" Digite + para ADIÇÃO")
        print(" Digite - para SUBTRAÇÃO")
        print(" Digite * para MULTIPLICAÇÃO")
        print(" Digite / para DIVISÃO")
        print(" Digite % para PORCENTAGEM\n")
        operador = mod_inputs.recebe_str("Digite um operador acima: ")
        if operador in ("+", "-", "*", "/", "%"):
            break
        else:
            print("\nOperador inválido!\n")
    return operador

def realiza_calculo(num1, num2, operador):
    match operador:
        case "+":
            resultado = num1 + num2
        case "-":
            resultado = num1 - num2
        case "*":
            resultado = num1 * num2
        case "/":
            resultado = num1 / num2
        case "%":
            resultado = num1 * num2 / 100
    return resultado

def mensagem_final():


def main():
    start = True
    while start:
        mod_msg.msg_calc_ini()
        num1 = mod_inputs.recebe_float("Digite o primeiro número: ")
        num2 = mod_inputs.recebe_float("Digite o segundo número: ")
        operador = valida_operador()
        resultado = realiza_calculo(num1, num2, operador)
        
        print("O resultado é = ", resultado)

if __name__ == "__main__":
    main()