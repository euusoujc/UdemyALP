N = int(input("Quantos elementos terao no vetor? "))

vet = []
abaixo_da_media = []

for i in range(N):
    num = float(input("Digite um numero: "))
    vet.append(num)

media = sum(vet) / N

abaixo_da_media = [num for num in vet if num < media]

print(f"MEDIA DO VETOR = {media}")
print(f"ELEMENTOS ABAIXO DA MEDIA:\n {abaixo_da_media}")
