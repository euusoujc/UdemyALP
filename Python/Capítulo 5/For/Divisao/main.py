n = int(input("Quantos numeros voce vai digitar? "))

for i in range(n):
    x = int(input("Entre com o numerador: "))
    y = int(input("Entre com o denominador: "))
    if y == 0:
        print("Divisão impossível")
    else:
        divisao = x / y
        print(f"DIVISAO = {divisao:.2f}")
