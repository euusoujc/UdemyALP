senha = int(input("Digite a senha: "))

while senha != 2002:
    print("Senha Invalida! Tente novamente:")
    senha = int(input())
if senha == 2002:
    print("Acesso permitido")
