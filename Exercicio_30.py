real = float(input("Digite o valor em reais: "))
cotacao = float(input("Digite a cotacao do dolar: "))

conversao = real / cotacao

print(f"{round(real, 2)} reais convertido em dólar são {round(conversao, 2)} dólares")
