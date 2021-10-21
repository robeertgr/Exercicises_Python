salarioBase = float(input("Digite o salário base do funcionário: "))

calculo = (salarioBase * 1.05) * 0.93

print(f"O salario R$ {round(salarioBase, 2)} com gratificação de 5%\n"
      f"e desconto de 7% de imposto é R$ {round(calculo, 2)}")
