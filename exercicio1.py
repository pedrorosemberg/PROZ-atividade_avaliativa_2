def calculo_cafe (a,b):
   return a  * b
    
print("Bem vindo a cafeteria cof-cof ")
print("------------------------------")

print("qual o valor do seu café?")
valor = int(input())

print("quantos você quer comprar?")
quantidade = int(input())

resultado = calculo_cafe (valor, quantidade)

print("o valor a ser pago é de:" , resultado)
