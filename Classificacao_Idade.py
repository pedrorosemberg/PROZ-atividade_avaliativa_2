

print("Digite seu nome :")
nome = input()

print("Digite sua Idade: ")
idade = int(input())

def classificar_idade (idade):

    if idade <12:
        return "Criança"
    elif 12<= idade <=17:
        return "Adolecente"
    elif 18<= idade <=40:
        return "Adulto Jovem "
    elif 40<= idade <=100:
        return "Adulto"

resultado = classificar_idade (idade)
print("Olá,",nome,"você foi classificado como,:",resultado,)