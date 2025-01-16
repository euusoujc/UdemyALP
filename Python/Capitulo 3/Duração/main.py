def converter_tempo(segundos_totais):
    horas = segundos_totais // 3600
    minutos = (segundos_totais % 3600) // 60
    segundos = segundos_totais % 60
    return horas, minutos, segundos


x = int(input("Digite a duração em segundos: "))

horas, minutos, segundos = converter_tempo(x)

print(f"{horas}:{minutos}:{segundos}")
