nome = str(input("Digite o nome: "))
valor_hora = float(input("Digite o valor recebido por hora: "))
horas = int(input("Digite as horas trabalhadas: "))

pagamento = valor_hora * horas

print(f"Nome: {nome}")
print(f"O pagamento de {nome} é de R$ {pagamento:.2f}")
