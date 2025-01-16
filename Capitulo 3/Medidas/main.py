import math


def area_quadrado(A):
    return pow(A, 2)


def area_triangulo(A, B):
    return (A * B) / 2


def area_trapezio(A, B, C):
    return (A + B) * C / 2


A = float(input("Digite a medida A: "))
B = float(input("Digite a medida B: "))
C = float(input("Digite a medida C: "))

areaQuad = area_quadrado(A)
areaTri = area_triangulo(A, B)
areaTrap = area_trapezio(A, B, C)

print(f"Area do quadrado: {areaQuad:.4f}")
print(f"Area do triângulo: {areaTri:.4f}")
print(f"Area do trapézio: {areaTrap:.4f}")
