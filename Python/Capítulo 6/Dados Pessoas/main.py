def qtd_homens(genero):
    male = 0
    for g in genero:
        if g.upper() == 'M':
            male += 1
    return male


def media_altura(altura, genero):
    soma_alturas = 0
    quant = 0

    for i in range(len(genero)):
        if genero[i] == 'F':
            soma_alturas += altura[i]
            quant += 1
        return soma_alturas / quant


N = int(input("Quantas pessoas serão digitadas? "))

altura = []
genero = []

for i in range(N):
    height = float(input(f"Altura da {i + 1}ª pessoa: "))
    gender = str(input(f"Genero da {i + 1}ª pessoa:(M/F) ")).strip().upper()

    altura.append(height)
    genero.append(gender)

menor_altura = min(altura)
maior_altura = max(altura)
quantidade_homens = qtd_homens(genero)
altura_mulheres = media_altura(altura, genero)

print(f"Menor altura = {menor_altura:.2f}")
print(f"Maior altura: {maior_altura:.2f}")
print(f"Media das alturas das mulheres = {altura_mulheres:.2f}")
print(f"Numero de homens = {quantidade_homens}")
