def valor_conta(plano, minutos):
    if minutos > 100:
        excedente = minutos - 100
        valor_total = plano + (excedente * 2.0)
    else:
        valor_total = plano
    return valor_total


plano = 50.00
minutos = int(input("Digite a quantidade de minutos: "))
valor_total = valor_conta(plano, minutos)

print(f"Valor a pagar: {valor_total:.2f}")
