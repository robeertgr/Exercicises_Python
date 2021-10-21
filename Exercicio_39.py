importancia = 700000

primeiroGanhador = importancia * 0.46
segundoGanhador = importancia * 0.32
terceiroGanhador = importancia - (primeiroGanhador + segundoGanhador)

print(f"A importancia de R$ {round(importancia, 2)} foi divida em três ganhadores:\n"
      f"O primeiro recebeu R$ {round(primeiroGanhador, 2)}\n"
      f"O segundo recebeu R$ {round(segundoGanhador, 2)}\n"
      f"O terceiro recebeu R$ {round(terceiroGanhador, 2)}")
