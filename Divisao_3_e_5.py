print("Digite um numero")
numero = int(input())

def divisivel_3_e_5(numero):
    if numero % 3 == 0 and numero % 5 == 0:
        return"O numero e divivel por 3 e 5"
    else:
        return"O numero não e divisivel por 3 e 5"

resultado = divisivel_3_e_5 (numero)

print("o numero,",numero,resultado)