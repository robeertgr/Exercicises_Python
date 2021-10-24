segundos = int(input("Digite um valor em segundos: "))

minutos = segundos / 60
horas = segundos / 3600

print(f"O valor em segundos é: {round(segundos, 0)} segundos ")
print(f"O valor em minutos é: {round(minutos, 0)} minutos ")
print(f"O valor em horas é: {round(horas, 0)} horas ")