def mais_velho(nomes, idade):
    maior_idade = max(idade)
    indice = idade.index(maior_idade)
    nome_mais_velho = nomes[indice]
    return nome_mais_velho


pessoas = int(input("Quantas pessoas voce vai digitar? "))

nomes = []
idade = []

for i in range(pessoas):
    print(f"Dados da {i + 1}ª pessoa: ")
    name = str(input("Nome: "))
    age = int(input("Idade: "))
    nomes.append(name)
    idade.append(age)

pessoa_mais_velha = mais_velho(nomes, idade)

print(f"Pessoa mais velha: {pessoa_mais_velha}")
