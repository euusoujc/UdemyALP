print("Digite as coordenadas de X e Y: ")
x = int(input())
y = int(input())

while x or y != 0:
    if x > 0 and y > 0:
        print("QUADRANTE Q1")
        break
    elif x < 0 and y > 0:
        print("QUADRANTE Q2")
        break
    elif x < 0 and y < 0:
        print("QUADRANTE Q3")
        break
    elif x > 0 and y < 0:
        print("QUADRANTE Q4")
        break
