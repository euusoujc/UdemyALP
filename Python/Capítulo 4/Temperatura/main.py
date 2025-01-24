def converter_temperatura(escala, temperatura):
    if escala.upper() == "C":
        return (temperatura * 1.8) + 32
    elif escala.upper() == "F":
        return (temperatura - 32) / 1.8


print("Digite a escala de temperatura (C para Celsius, F para Fahrenheit): ")
escala = input().strip().upper()

print(f"Digite a temperatura em {escala}: ")
temperatura = float(input())
resultado = converter_temperatura(escala, temperatura)

if escala == "C":
    print(f"A temperatura em Fahrenheit é: {resultado:.2f}")
else:
    print(f"A temperatura em Celsius é: {resultado:.2f}")
