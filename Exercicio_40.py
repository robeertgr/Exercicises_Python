diasTrabalhados = float(input("Digite a quantidade de dias trabalhados: "))

valorTrabalhado = 30
valorRecebido = (diasTrabalhados * valorTrabalhado) * 0.92

print(f"A quantia paga pelos {diasTrabalhados} dias trabalhados com desconto\n"
      f"de 8% de imposto de renda foi R$ {valorRecebido}")
