num = int(input("Digite um numero inteiro (100 a 999) com 3 digitos: "))

while num < 100 or num > 999:
    num = int(input("Digite um numero inteiro (100 a 999) com 3 digitos: "))

num = str(num)
reverse = num[::-1]

print(f"O numero {num} digitado ao contrário é: {reverse}")
