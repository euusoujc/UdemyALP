N = int(input("Quantos numeros voce vai digitar? "))

vet = []
contagem = 0

for i in range(N):
    x = int(input("Digite um numero: "))
    if x % 2 == 0:
        vet.append(x)
        contagem += 1
print(f"Numeros pares:\n {vet}")
print(f"Quantidade de pares = {contagem}")
