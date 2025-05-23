print("print bem vindo ao calculador de descontos")
print("------------------------------------------")

def calculo (a,b):
   return (a * b) /100 

print("digite o valor do produto:")
vp = float(input())

print("digite o desconto:")
vd = float(input())

resultado = calculo (vp , vd)
print("O produto vai custar:", vp -resultado )