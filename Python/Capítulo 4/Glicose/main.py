glicose = float(input("Digite a medida da glicose: "))

if glicose <= 100:
    print("Normal")
elif glicose <= 140:
    print("Elevado")
else:
    print("Diabetes")
