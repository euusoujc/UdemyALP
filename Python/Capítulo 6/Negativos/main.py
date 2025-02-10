n = int(input("Quantos números voce vai digitar? "))
vet = []
while n <= 10:
    for i in range(n):
        x = int(input(f"Digite um numero: "))
        vet.append(x)

    print("\nNumeros negativos: ")
    for num in vet:
        if num < 0:
            print(num)
