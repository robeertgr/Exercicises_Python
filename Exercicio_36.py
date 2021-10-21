altura = float(input("Digite a altura do cilindro: "))
raio = float(input("Digite o raio do cilindro: "))

volume = 3.14 * ((raio * raio) * altura)

print(f"O volume do cilindro com altura {altura} e raio {raio} é {round(volume, 2)}")
