num = int(input("Digite um numero de 1000 a 9999: "))

while num < 1000 or num > 9999:
    num = int(input("Digite um número de 1000 a 9999: "))

print(f"O primeiro digito: ")
print(f"O primeiro digito: {str(num)[1]}")
print(f"O primeiro digito: {str(num)[2]}")
print(f"O primeiro digito: {str(num)[3]}")
