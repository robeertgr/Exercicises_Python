comprimento = float(input("Comprimento do terreno: "))
largura = float(input("Largura do terreno: "))
preco = float(input("Preço do metro de tela: "))

gasto = (2 * comprimento + 2 * largura) * preco

print(f"O preço para cercar o terreno com telas é R$ {round(gasto, 2)}")
