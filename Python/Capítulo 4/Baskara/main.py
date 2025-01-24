import math


def eq_segundo_grau(a, b, c):

    if a == 0:
        print("O valor de 'a' deve ser diferente de zero para uma equação do segundo grau.")
        return

    Delta = b ** 2 - 4 * a * c

    if Delta == 0:
        raiz = -b / (2 * a)  # Raiz única
        print(f"A equação possui uma raiz única: {raiz:.2f}")

    elif Delta > 0:
        raiz1 = (-b + math.sqrt(Delta)) / (2 * a)
        raiz2 = (-b - math.sqrt(Delta)) / (2 * a)
        print(f"A equação possui duas raízes reais: {raiz1:.2f} e {raiz2:.2f}")

    else:
        print("A equação não possui raízes reais.")


try:
    a = float(input("Digite o valor de A: "))
    b = float(input("Digite o valor de B: "))
    c = float(input("Digite o valor de C: "))

    eq_segundo_grau(a, b, c)

except ValueError:
    print("Por favor, insira valores numéricos válidos.")
