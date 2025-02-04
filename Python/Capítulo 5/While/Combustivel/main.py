codigo = 0
alcool = gasolina = diesel = 0


print("Informe um codigo (1, 2, 3) ou 4 para parar: ")


while codigo != 4:
    codigo = int(input())
    while codigo < 1 and codigo > 4:
        codigo = int(input())
    if codigo == 1:
        alcool += 1
    elif codigo == 2:
        gasolina += 1
    elif codigo == 3:
        diesel += 1

print(f"MUITO OBRIGADO\n Alcool: {alcool}\nGasolina: {
      gasolina}\nDiesel: {diesel}")
