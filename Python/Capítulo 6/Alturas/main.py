def calcular_altura_media(vet):
    alt_media = 0
    for i in range(N):
        alt_media += vet[i][2] / N
    return alt_media


def menor_de_16(vet):
    count = 0
    for i in range(N):
        if vet[i][1] < 16:
            count += 1
    porcentagem = (count * 100) / N
    return porcentagem


def nomes_menores_de_16(vet):
    nomes = []
    for i in range(N):
        if vet[i][1] < 16:
            nomes.append(vet[i][0])
    return nomes


N = int(input("Quantas pessoas serao digitadas? "))

vet = []

for i in range(N):
    print(f"Dados da {i + 1}ª pessoa")
    nome = str(input("Nome: "))
    idade = int(input("Idade: "))
    altura = float(input("Altura: "))
    vet.append((nome, idade, altura))

media = calcular_altura_media(vet)
menores = menor_de_16(vet)
nomes_menores = nomes_menores_de_16(vet)


print(f"\nAltura média: {media:.2f}")
print(f"Pessoas com menos de 16 anos: {menores:.1f}")
if nomes_menores:
    print(f"\nPessoas com menos de 16 anos:{nomes_menores}")
else:
    print("Nenhuma pessoa tem menos de 16 anos.")
