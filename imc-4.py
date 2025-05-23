# Calculo de IMC
# 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 13, 15, 16

print("Vamos calcular o seu Índice de Massa Corporal (IMC)?")

#Peso em quilogramas (kg)
print("Por favor, digite o seu peso (em Kg): ")
peso = float(input())

#Altura em metros (m)
print("Agora, digite sua altura (em metros): ")
altura = float(input())

#Calcula o IMC
# IMC = peso / (altura * altura)
imc = peso / (altura * altura)

# Menor que 18,5	Baixo peso
# De 18,5 a 24,9	Peso normal
# De 25 a 29,9	Sobrepeso
# De 30 a 34,9	Obesidade grau I
# De 35 a 39.9	Obesidade grau II
# Igual ou maior que 40	Obesidade grau III

# Mostra o resultado
if imc < 18.5:
    print(f"Você está com *PESO BAIXO*! Seu Índice de Massa Corporal é {imc}. Vamos comer um pouquinho mais?")
    
elif imc >= 18.5 and imc <= 24.9:
    print(f"Você está com *PESO NORMAL*! Seu Índice de Massa Corporal é {imc}. Nada mal, hein?!")

elif imc >= 25 and imc <= 29.9:
    print(f"Você está com *SOBREPESO*! Seu Índice de Massa Corporal é {imc}. Vamos comer um pouco menos?")

elif imc >= 30 and imc <= 34.9:
    print(f"Você está com *OBESIDADE GRAU I*! Seu Índice de Massa Corporal é {imc}. Ó Márcia, me trás aí um cadeado...")
    
elif imc >= 35 and imc <= 39.9:
    print(f"Você está com *OBESIDADE GRAU II*! Seu Índice de Massa Corporal é {imc}. Ó, Márcia, acho que vamos precisar costurar a boca de alguém.")

else:
    print("Irmão, é só digitar o seu peso e sua altura. Tendi foi nada.")