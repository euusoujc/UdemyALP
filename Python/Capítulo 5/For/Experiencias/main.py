n = int(input("Quantos casos de testes serão digitados? "))
rato = 0
sapo = 0
coelho = 0
contagem = 0

for i in range(n):
    cobaias = int(input("Quantidade de cobaias: "))
    tipo = str(input("Tipo de cobaia:(R/C/S) "))
    contagem += cobaias
    if tipo == "R":
        rato += cobaias
    elif tipo == "C":
        coelho += cobaias
    elif tipo == "S":
        sapo += cobaias

print("Total: %d cobaias" % contagem)
print("Total de coelhos: %d" % coelho)
print("Total de ratos: %d" % rato)
print("Total de sapos: %d" % sapo)
print("Percentual de coelhos: %.2f" % float(((100*coelho)/contagem)), '%')
print("Percentual de ratos: %.2f" % float(((100*rato)/contagem)), '%')
print("Percentual de sapos: %.2f" % float(((100*sapo)/contagem)), '%')
