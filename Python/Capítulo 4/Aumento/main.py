salario_atual = float(input("Digite o salario da pessoa: "))

if salario_atual <= 1000.00:
    porcentagem = "20%"
    aumento = salario_atual * 0.20
    novo_salario = salario_atual + aumento
elif salario_atual <= 3000.00:
    porcentagem = "15%"
    aumento = salario_atual * 0.15
    novo_salario = salario_atual + aumento
elif salario_atual <= 8000.00:
    porcentagem = "10%"
    aumento = salario_atual * 0.10
    novo_salario = salario_atual + aumento
else:
    porcentagem = "5%"
    aumento = salario_atual * 0.05
    novo_salario = salario_atual + aumento

print(f"Novo salario = {novo_salario:.2f}")
print(f"Aumento = {aumento}")
print(f"Porcentagem = {porcentagem} ")
