largura = float(input("Digite a largura do terreno: "))
comprimento = float(input("Digite o comprimento do terreno: "))
valor = float(input("Digite o valor do metro quadrado: "))

area = largura * comprimento
preco = valor * area

print(f"Area do terreno: {area}")
print(f"Preço do terreno: {preco}")
