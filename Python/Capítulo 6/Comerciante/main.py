def lucro_menor10(valor_compra, valor_venda):
    contador = 0
    for i in range(len(valor_compra)):
        lucro = ((valor_venda[i] - valor_compra[i]) / valor_compra[i]) * 100
        if lucro < 10:
            contador += 1
    return contador


def lucro_entre10e20(valor_compra, valor_venda):
    contador = 0
    for i in range(len(valor_compra)):
        lucro = ((valor_venda[i] - valor_compra[i]) / valor_compra[i]) * 100
        if 10 <= lucro <= 20:
            contador += 1
    return contador


def lucro_maior20(valor_compra, valor_venda):
    contador = 0
    for i in range(len(valor_compra)):
        lucro = ((valor_venda[i] - valor_compra[i]) / valor_compra[i]) * 100
        if lucro > 20:
            contador += 1
    return contador


N = int(input("Quantos produtos serao digitados? "))

produto = []
valor_compra = []
valor_venda = []

for i in range(N):
    name = str(input("Produto: "))
    buy_price = float(input("Preço de compra: "))
    sell_price = float(input("Preço de venda: "))

    produto.append(name)
    valor_compra.append(buy_price)
    valor_venda.append(sell_price)

total_compra = sum(valor_compra)
total_venda = sum(valor_venda)
lucro_total = total_venda - total_compra

print(f"Lucro abaixo de 10%: {lucro_menor10(valor_compra, valor_venda)}")
print(f"Lucro entre 10% e 20%: {lucro_entre10e20(valor_compra, valor_venda)}")
print(f"Lucro acima de 20%: {lucro_maior20(valor_compra, valor_venda)}")
print(f"Valor total de compra: {total_compra:.2f}")
print(f"Valor total de venda: {total_venda:.2f}")
print(f"Lucro total: {lucro_total:.2f}")
