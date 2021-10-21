import math

a = float(input("Digite o valor de A: "))
b = float(input("Digite o valor de B: "))

hipotenusa = math.sqrt((a * a) + (b * b))

print(f"O valor da hipotenusa recebendo os valores A = {a} e B = {b} é {hipotenusa}")
