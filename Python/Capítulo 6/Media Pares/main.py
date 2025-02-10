def calcular_media(pares):
    if len(pares) == 0:
        return None

    media = sum(pares) / len(pares)
    return media


N = int(input("Quantos elementos terão no vetor? "))

pares = []

for i in range(N):
    x = int(input("Digite um numero: "))
    if x % 2 == 0:
        pares.append(x)

media_dos_pares = calcular_media(pares)

if media_dos_pares is not None:
    print(f"MEDIA DOS PARES = {media_dos_pares:.1f}")
else:
    print("NENHUM NUMERO PAR")
