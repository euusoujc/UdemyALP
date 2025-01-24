hora_inicial = int(input("Hora inicial: "))
hora_final = int(input("Hora final: "))
duracao = int

if hora_inicial < hora_final:
    duracao = hora_final - hora_inicial
elif hora_inicial > hora_final:
    duracao = (24 - hora_inicial) + hora_final
else:
    duracao = 24

print(f"O jogo durou {duracao} hora(s)")
