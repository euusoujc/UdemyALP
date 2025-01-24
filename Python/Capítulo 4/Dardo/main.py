print("Digite as três distâncias: ")
x = float(input())
y = float(input())
z = float(input())

if x > y and z:
    maior = x
if y > x and z:
    maior = y
else:
    maior = z

print(f"MAIOR DISTANCIA: {maior:.2f}")
