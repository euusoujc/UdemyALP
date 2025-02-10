def aprovados(nomes, nota_um, nota_dois):
    nomes_aprovados = []

    for i in range(len(nomes)):
        media = (nota_um[i] + nota_dois[i]) / 2

        if media >= 6:
            nomes_aprovados.append(nomes[i])

    return nomes_aprovados


N = int(input("Quantos alunos serao digitados? "))

nomes = []
nota_um = []
nota_dois = []

for i in range(N):
    print(f"Digite nome, primeira e segunda nota do {i + 1}° aluno")
    name = str(input())
    primeira_nota = float(input())
    segunda_nota = float(input())

    nomes.append(name)
    nota_um.append(primeira_nota)
    nota_dois.append(segunda_nota)

alunos_aprovados = aprovados(nomes, nota_um, nota_dois)

if alunos_aprovados:
    print("\nAlunos aprovados:")
    for aluno in alunos_aprovados:
        print(aluno)
else:
    print("\nNenhum aluno foi aprovado.")
