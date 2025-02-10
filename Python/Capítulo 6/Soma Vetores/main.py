N = int(input("Quantos valores terão em cada vetor? "))

vet_A = []
vet_B = []
vet_C = []

for i in range(N):
    valor_A = int(input("Digite os valores de A: "))
    vet_A.append(valor_A)

for i in range(N):
    valor_B = int(input("Digite os valores de B: "))
    vet_B.append(valor_B)

for i in range(N):
    vet_C.append(vet_A[i] + vet_B[i])

print(f"Vetor resultante:\n {vet_C}")
