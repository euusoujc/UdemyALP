n = int(input("Digite o valor de N: "))
fat = 1

for i in range(n):
    if n > 15:
        break
    else:
        fat = fat * (n - i)

print(f"FATORIAL = {fat}")
