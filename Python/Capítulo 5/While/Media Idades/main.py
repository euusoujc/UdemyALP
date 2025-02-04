x = int(input("Digite as idades: "))

if x < 0:
    print("IMPOSSIVEL CALCULAR")
else:
    soma = 0
    contador = 0

    while x >= 0:
        soma += x
        contador += 1
        x = int(input())

    media = soma / contador
    print(f"MEDIA = {media:.2f}")
