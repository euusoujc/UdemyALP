codigo = int(input("Digite o código do produto: "))
quantidade = int(input("Digite a quantidade: "))
valor_total = float

if codigo == 1:
    valor_total = quantidade * 5.00
elif codigo == 2:
    valor_total = quantidade * 3.50
elif codigo == 3:
    valor_total = quantidade * 4.80
elif codigo == 4:
    valor_total = quantidade * 8.90
else:
    valor_total = quantidade * 7.32

print(f"Valor a pagar: {valor_total:.2f}")
