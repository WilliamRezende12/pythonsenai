import mod_inputs
import mod_sair

start = True
while start:
    nome = mod_inputs.inp_str("\nDigite seu nome: ")
    idade = mod_inputs.inp_int("\nDigite sua idade em anos: ")
    peso = mod_inputs.inp_float("\nDigite seu peso em KG: ")

    print("\n================== Dados Informados ==================")
    print("Seu nome é:", nome)
    print("Você possui", idade, "anos de idade.")
    print("Seu peso é", peso, "KG.")

    start = mod_sair.finalizar()