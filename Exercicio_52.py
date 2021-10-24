premio = float(input("Digite o valor do prêmio:\n"))
investimento1 = float(input("Digite o investimento do apostador 1:\n"))
investimento2 = float(input("Digite o investimento do apostador 2:\n"))
investimento3 = float(input("Digite o investimento do apostador 3:\n"))

total_aposta = investimento1 + investimento2 + investimento3

prop_investimento1 = investimento1 / total_aposta
prop_investimento2 = investimento2 / total_aposta
prop_investimento3 = investimento3 / total_aposta

premio_investimento1 = prop_investimento1 * premio
premio_investimento2 = prop_investimento2 * premio
premio_investimento3 = prop_investimento3 * premio

print(f"O prêmio do apostador 1 é: {round(premio_investimento1, 2)}")
print(f"O prêmio do apostador 2 é: {round(premio_investimento2, 2)}")
print(f"O prêmio do apostador 3 é: {round(premio_investimento3, 2)}")
