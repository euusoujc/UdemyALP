n = int(input("Quantos números voce vai digitar? "))

dentro = 0
fora = 0

for i in range(n):
    x = int(input())
    if 10 <= x <= 20:
        dentro += 1
    else:
        fora += 1
print(f"{dentro} DENTRO")
print(f"{fora} FORA")
