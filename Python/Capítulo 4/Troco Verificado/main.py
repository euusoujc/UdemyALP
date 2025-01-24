def verificar(dinheiro_recebido, valor_total):
    if dinheiro_recebido < valor_total:
        valor_restante = valor_total - dinheiro_recebido
        print(f"DINHEIRO INSUFICIENTE. FALTAM = {valor_restante:.2f}")
    else:
        troco = dinheiro_recebido - valor_total
        print(f"TROCO = {troco:.2f}")


preco_produto = float(input("Preço unitário do produto: "))
quantidade = float(input("Quantidade comprada: "))
dinheiro_recebido = float(input("Dinheiro recebido: "))
valor_total = preco_produto * quantidade

verificar(dinheiro_recebido, valor_total)
