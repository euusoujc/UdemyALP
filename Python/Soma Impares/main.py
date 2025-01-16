def somaImpar(x, y):
    soma = 0
    for i in range(min(x, y) + 1, max(x, y)):
        if i % 2 != 0:
            soma += i
    return soma


print("Digite dois números: ")
x = int(input())
y = int(input())

soma = somaImpar(x, y)
print(f"SOMA = {soma}")
