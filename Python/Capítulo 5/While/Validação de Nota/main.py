while True:
    x = float(input("Digite a primeira nota: "))
    if x < 0 or x > 10:
        print("Valor invalido! Tente novamente.")
        continue

    y = float(input("Digite a segunda nota: "))
    if y < 0 or y > 10:
        print("Valor invalido! Tente novamente.")
        continue

    media = (x + y) / 2
    print(f"MEDIA = {media:.2f}")
    break
