print("Vamos calcular os juros simples desse investimento aí, fera?")
print("Vem comigo! \nVamos começar 'simples'... \nPrimeiro, me fala aí o valor que você tem (em R$): ")
capital = float(input())

print("Show! Agora me fala qual a merreca da taxa de juros que o banco quer te pagar (em % ao período): ")
taxa_percentual = float(input())
taxa = taxa_percentual / 100  # Convertendo de percentual para decimal

print("Deixar seu dinheiro parado rende mais do que isso, aí... \nE quanto tempo você quer deixar? (Considere o mesmo período que os juros serão pagos...)")
tempo = float(input())

juros = capital * taxa * tempo
montante = capital + juros

print(f"Se liga na mixaria que vai ser isso aqui, patrão: R$ {juros:.2f}")
print(f"E no final do período, você vai ter um montante de: R$ {montante:.2f}")
