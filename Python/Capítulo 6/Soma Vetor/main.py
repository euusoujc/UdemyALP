def calcular_media(vet):
    media = 0
    for i in range(vet):
        media += i / vet
    return media


def calcular_soma(vet):
    soma = 0
    for i in range(vet):
        soma += i
    return soma


N = int(input("Quantos numeros voce vai digitar? "))

vet = []

for i in range(N):
    num = float(input("Digite um numero: "))
    vet.append(num)

media = calcular_media(vet)
soma = calcular_soma(vet)

print(f"Valores = {vet}")
print(f"Soma = {soma}")
print(f"Media = {media:.2f}")
