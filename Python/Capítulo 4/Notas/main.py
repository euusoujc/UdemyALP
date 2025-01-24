nota_1 = float(input("Digite a primeira nota: "))
nota_2 = float(input("Digite a segunda nota: "))
nota_final = nota_1 + nota_2

if nota_final < 60:
    print(f"Nota final: {nota_final:.1f}")
    print(f"REPROVADO")
else:
    print(f"Nota final: {nota_final:.1f}")
    print(f"APROVADO")
