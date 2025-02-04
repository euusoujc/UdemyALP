n = int(input("Quantos casos voce vai digitar? "))

for i in range(n):
    print(f"Digite os três valores do caso: ")
    x1 = float(input())
    x2 = float(input())
    x3 = float(input())

    peso1 = 2
    peso2 = 3
    peso3 = 5

    media = (x1 * peso1 + x2 * peso2 + x3 * peso3) / (peso1 + peso2 + peso3)

    print(f"MEDIA = {media:.2f}")
