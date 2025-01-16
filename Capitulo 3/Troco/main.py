preco = float(input("Preço unitário: "))
qntd = int(input("Quantidade comprada: "))
valor = float(input("Dinheiro recebido: "))

total = preco * qntd
troco = valor - total

print(f"Troco: {troco:.2f}")
