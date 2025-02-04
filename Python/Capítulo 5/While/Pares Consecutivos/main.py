x = int(input("Digite um número inteiro: "))

while x != 0:
    if x % 2 != 0:
        x += 1

    soma = 0

    for i in range(5):
        soma += x
        x += 2

    print(f"SOMA = {soma}")
