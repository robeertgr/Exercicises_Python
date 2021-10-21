valorTotal = float(input("Digite o valor total do produto: R$ "))

valorComDesconto = valorTotal * 0.90
valorDasParcelas = valorTotal / 3.0
comissaoVista = valorComDesconto * 0.05
comissaoParcelado = valorTotal * 0.05

print(f"Valor a ser pago com desconto de 10%: R$ {round(valorComDesconto, 2)}\n"
      f"Valor das parcelas em três vezes: R$ {round(valorDasParcelas, 2)}\n"
      f"Comissão do vendedor de cinco porcento à vista: R$ {round(comissaoVista, 2)}\n"
      f"Comissão do vendedor de cinco porcento à prazo: R$ {round(comissaoParcelado, 2)}")
