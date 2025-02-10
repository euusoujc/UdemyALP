N = int(input("Quantos numeros voce vai digitar? "))
vet = []

for i in range(N):
    x = float(input("Digite um numero: "))
    vet.append(x)

print(f"Maior valor = {max(vet)}")
print(f"Posição do maior valor = {vet.index(max(vet))}")
