valorHoraTrabalhada = float(input("Digite o valor das horas trabalhadas: "))
numeroHorasTrabalhada = int(input("Digite as horas trabalhadas: "))

valorCalculado = (valorHoraTrabalhada * numeroHorasTrabalhada) * 1.10

print(f"Valor da hora trabalhada: R$ {round(valorHoraTrabalhada, 2)}\n"
      f"Horas trabalhadas no mês: {numeroHorasTrabalhada}\n"
      f"O valor calculado com acrescimo de 10% é R$ {round(valorCalculado, 2)}")
